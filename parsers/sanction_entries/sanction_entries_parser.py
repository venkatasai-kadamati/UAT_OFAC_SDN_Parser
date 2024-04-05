import csv
from lxml import etree

# namespace and xpath definition
namespace = {"ns": "http://www.un.org/sanctions/1.0"}


def parse_sanctions_entries(xml_path, csv_file):
    tree = etree.parse(xml_path)
    root = tree.getroot()

    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "SanctionsEntryID",
                "ProfileID",
                "ListID",
                "EntryEventID",
                "EntryEventTypeID",
                "LegalBasisID",
                "EntryEventComment",
                "EntryEventDate",
                "SanctionsMeasureID",
                "SanctionsTypeID",
                "SanctionsMeasureComment",
                "DatePeriodFixed",
            ]
        )

        # Iterate over each SanctionsEntry element
        for sanctions_entry in root.findall(
            "ns:SanctionsEntries/ns:SanctionsEntry", namespaces=namespace
        ):
            entry_id = sanctions_entry.get("ID")
            profile_id = sanctions_entry.get("ProfileID")
            list_id = sanctions_entry.get("ListID")

            # EntryEvent details
            entry_event = sanctions_entry.find("ns:EntryEvent", namespaces=namespace)
            entry_event_id = entry_event.get("ID")
            entry_event_type_id = entry_event.get("EntryEventTypeID")
            legal_basis_id = entry_event.get("LegalBasisID")
            entry_event_comment = entry_event.findtext(
                "ns:Comment", namespaces=namespace, default=""
            )
            entry_event_date = "-".join(
                [
                    entry_event.findtext(
                        "ns:Date/ns:Year", namespaces=namespace, default=""
                    ),
                    entry_event.findtext(
                        "ns:Date/ns:Month", namespaces=namespace, default=""
                    ),
                    entry_event.findtext(
                        "ns:Date/ns:Day", namespaces=namespace, default=""
                    ),
                ]
            )

            # SanctionsMeasure details
            for sanctions_measure in sanctions_entry.findall(
                "ns:SanctionsMeasure", namespaces=namespace
            ):
                sanctions_measure_id = sanctions_measure.get("ID")
                sanctions_type_id = sanctions_measure.get("SanctionsTypeID")
                sanctions_measure_comment = sanctions_measure.findtext(
                    "ns:Comment", namespaces=namespace, default=""
                )
                date_period_fixed = sanctions_measure.find(
                    "ns:DatePeriod", namespaces=namespace
                ).get("YearFixed", "false")

                writer.writerow(
                    [
                        entry_id,
                        profile_id,
                        list_id,
                        entry_event_id,
                        entry_event_type_id,
                        legal_basis_id,
                        entry_event_comment,
                        entry_event_date,
                        sanctions_measure_id,
                        sanctions_type_id,
                        sanctions_measure_comment,
                        date_period_fixed,
                    ]
                )

    print(f"Data successfully written to {csv_file}")


# Specify the path to your XML file and the output CSV file
xml_path = "source/sdn_advanced.xml"
csv_file = "parsers/sanction_entries/sanctions_entries.csv"
parse_sanctions_entries(xml_path, csv_file)
