import csv
from lxml import etree

# Define the namespace map based on the XML structure.
namespace = {"ns": "http://www.un.org/sanctions/1.0"}


def parse_document_dates(id_reg_document):
    document_dates_info = []
    for document_date in id_reg_document.findall(
        "ns:DocumentDate", namespaces=namespace
    ):
        date_type_id = document_date.get("IDRegDocDateTypeID")
        date_period = document_date.find("ns:DatePeriod", namespaces=namespace)
        if date_period is not None:
            start_date = date_period.find("ns:Start/ns:From", namespaces=namespace)
            end_date = date_period.find("ns:End/ns:To", namespaces=namespace)
            start_date_str = "-".join(
                [
                    start_date.findtext("ns:Year", namespaces=namespace, default=""),
                    start_date.findtext("ns:Month", namespaces=namespace, default=""),
                    start_date.findtext("ns:Day", namespaces=namespace, default=""),
                ]
            ).strip("-")
            end_date_str = "-".join(
                [
                    end_date.findtext("ns:Year", namespaces=namespace, default=""),
                    end_date.findtext("ns:Month", namespaces=namespace, default=""),
                    end_date.findtext("ns:Day", namespaces=namespace, default=""),
                ]
            ).strip("-")
            date_str = f"{date_type_id}: {start_date_str} to {end_date_str}"
            document_dates_info.append(date_str)
    return "; ".join(document_dates_info)


# Load the XML content from the file
xml_path = "source/sdn_advanced.xml"
tree = etree.parse(xml_path)
root = tree.getroot()

# Open the CSV file for writing
csv_file = "parsers/id_reg_document/id_reg_documents.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "ID",
            "IDRegDocTypeID",
            "IdentityID",
            "IssuedBy-CountryID",
            "ValidityID",
            "IDRegistrationNo",
            "IssuingAuthority",
            "DocumentedNameID",
            "DocumentDates",
        ]
    )

    # Iterate over each IDRegDocument element
    for id_reg_document in root.findall(
        "ns:IDRegDocuments/ns:IDRegDocument", namespaces=namespace
    ):
        id_value = id_reg_document.get("ID")
        id_reg_doc_type_id = id_reg_document.get("IDRegDocTypeID")
        identity_id = id_reg_document.get("IdentityID")
        issued_by_country_id = id_reg_document.get("IssuedBy-CountryID", "N/A")
        validity_id = id_reg_document.get("ValidityID", "N/A")
        id_registration_no = id_reg_document.findtext(
            "ns:IDRegistrationNo", namespaces=namespace, default="N/A"
        )
        issuing_authority = id_reg_document.findtext(
            "ns:IssuingAuthority", namespaces=namespace, default="N/A"
        )
        documented_name_reference = id_reg_document.find(
            "ns:DocumentedNameReference", namespaces=namespace
        )
        documented_name_id = (
            documented_name_reference.get("DocumentedNameID")
            if documented_name_reference is not None
            else "N/A"
        )
        document_dates = parse_document_dates(id_reg_document)

        writer.writerow(
            [
                id_value,
                id_reg_doc_type_id,
                identity_id,
                issued_by_country_id,
                validity_id,
                id_registration_no,
                issuing_authority,
                documented_name_id,
                document_dates,
            ]
        )

print(f"Data successfully written to {csv_file}")
