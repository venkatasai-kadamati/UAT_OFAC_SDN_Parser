import csv
from lxml import etree

# Define the namespace map based on the XML structure.
namespace = {"ns": "http://www.un.org/sanctions/1.0"}


def parse_distinct_party(xml_path, csv_file):
    tree = etree.parse(xml_path)
    root = tree.getroot()

    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Define the header with columns for each type of nested element
        header = [
            "DistinctPartyID",
            "ProfileID",
            # "PartySubTypeID",
            # "IdentityID",
            # "AliasTypeID",
            # "DocNameStatusID",
            # "NameParts",
            # "FeatureTypeID",
            # "FeatureVersionReliabilityID",
            # "FeatureVersionComment",
            # "FeatureVersionLocationID",
            "DatePeriodDetails",
        ]
        writer.writerow(header)

        # Iterate over each DistinctParty element
        for distinct_party in root.findall(
            "ns:DistinctParties/ns:DistinctParty", namespaces=namespace
        ):
            distinct_party_id = distinct_party.get("FixedRef")
            for profile in distinct_party.findall("ns:Profile", namespaces=namespace):
                profile_id = profile.get("ID")
                party_sub_type_id = profile.get("PartySubTypeID")
                for identity in profile.findall("ns:Identity", namespaces=namespace):
                    identity_id = identity.get("ID")
                    for alias in identity.findall("ns:Alias", namespaces=namespace):
                        alias_type_id = alias.get("AliasTypeID")
                        doc_name_status_id = alias.find(
                            "ns:DocumentedName", namespaces=namespace
                        ).get("DocNameStatusID")
                        name_parts = "; ".join(
                            name_part.text
                            for name_part in alias.findall(
                                "ns:DocumentedName/ns:DocumentedNamePart/ns:NamePartValue",
                                namespaces=namespace,
                            )
                        )
                        for feature in profile.findall(
                            "ns:Feature", namespaces=namespace
                        ):
                            feature_type_id = feature.get("FeatureTypeID")
                            for version in feature.findall(
                                "ns:FeatureVersion", namespaces=namespace
                            ):
                                reliability_id = version.get("ReliabilityID")
                                comment = version.findtext(
                                    "ns:Comment", namespaces=namespace, default="N/A"
                                )
                                location_element = version.find(
                                    "ns:VersionLocation", namespaces=namespace
                                )
                                location_id = (
                                    location_element.get("LocationID")
                                    if location_element is not None
                                    else "N/A"
                                )
                                date_period = extract_date_period(version, namespace)

                                writer.writerow(
                                    [
                                        distinct_party_id,
                                        profile_id,
                                        # party_sub_type_id,
                                        # identity_id,
                                        # alias_type_id,
                                        # doc_name_status_id,
                                        # name_parts,
                                        # feature_type_id,
                                        # reliability_id,
                                        # comment,
                                        # location_id,
                                        date_period,
                                    ]
                                )

    print(f"Data successfully written to {csv_file}")


def extract_date_period(feature_version, namespace):
    date_period_element = feature_version.find("ns:DatePeriod", namespaces=namespace)
    if date_period_element is not None:
        start_element = date_period_element.find(
            "ns:Start/ns:From", namespaces=namespace
        )
        end_element = date_period_element.find("ns:End/ns:To", namespaces=namespace)
        start_date = (
            "-".join(
                [
                    start_element.findtext("ns:Year", namespaces=namespace, default=""),
                    start_element.findtext(
                        "ns:Month", namespaces=namespace, default=""
                    ),
                    start_element.findtext("ns:Day", namespaces=namespace, default=""),
                ]
            )
            if start_element is not None
            else "N/A"
        )
        end_date = (
            "-".join(
                [
                    end_element.findtext("ns:Year", namespaces=namespace, default=""),
                    end_element.findtext("ns:Month", namespaces=namespace, default=""),
                    end_element.findtext("ns:Day", namespaces=namespace, default=""),
                ]
            )
            if end_element is not None
            else "N/A"
        )
        return f"Start: {start_date}, End: {end_date}"
    return "N/A"


# Specify the path to your XML file and the output CSV file
xml_path = "source/sdn_advanced.xml"
csv_file = "custom_parsers/dp_with_dob/dp_with_dob.csv"
parse_distinct_party(xml_path, csv_file)
