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
            "PartySubTypeID",
            "IdentityID",
            "AliasDetails",
            "FeatureDetails",
        ]
        writer.writerow(header)

        # Iterate over each DistinctParty element
        for distinct_party in root.findall(
            "ns:DistinctParties/ns:DistinctParty", namespaces=namespace
        ):
            distinct_party_id = distinct_party.get("FixedRef")
            alias_details_list = []
            feature_details_list = []

            for profile in distinct_party.findall("ns:Profile", namespaces=namespace):
                profile_id = profile.get("ID")
                party_sub_type_id = profile.get("PartySubTypeID")
                for identity in profile.findall("ns:Identity", namespaces=namespace):
                    identity_id = identity.get("ID")
                    for alias in identity.findall("ns:Alias", namespaces=namespace):
                        alias_type_id = alias.get("AliasTypeID")
                        primary = alias.get("Primary")
                        low_quality = alias.get("LowQuality")
                        documented_name_id = alias.find(
                            "ns:DocumentedName", namespaces=namespace
                        ).get("ID")
                        name_parts = "; ".join(
                            [
                                name_part.text
                                for name_part in alias.findall(
                                    "ns:DocumentedName/ns:DocumentedNamePart/ns:NamePartValue",
                                    namespaces=namespace,
                                )
                            ]
                        )
                        alias_details = f"TypeID: {alias_type_id}, Primary: {primary}, LowQuality: {low_quality}, DocNameID: {documented_name_id}, NameParts: {name_parts}"
                        alias_details_list.append(alias_details)

                    for feature in profile.findall("ns:Feature", namespaces=namespace):
                        feature_type_id = feature.get("FeatureTypeID")
                        for feature_version in feature.findall(
                            "ns:FeatureVersion", namespaces=namespace
                        ):
                            reliability_id = feature_version.get("ReliabilityID")
                            version_location_id = (
                                feature_version.find(
                                    "ns:VersionLocation", namespaces=namespace
                                ).get("LocationID", "N/A")
                                if feature_version.find(
                                    "ns:VersionLocation", namespaces=namespace
                                )
                                is not None
                                else "N/A"
                            )
                            feature_details = f"TypeID: {feature_type_id}, ReliabilityID: {reliability_id}, LocationID: {version_location_id}"
                            feature_details_list.append(feature_details)

            # Combine all alias and feature details into strings
            alias_details_str = " | ".join(alias_details_list)
            feature_details_str = " | ".join(feature_details_list)

            writer.writerow(
                [
                    distinct_party_id,
                    profile_id,
                    party_sub_type_id,
                    identity_id,
                    alias_details_str,
                    feature_details_str,
                ]
            )

    print(f"Data successfully written to {csv_file}")


# Specify the path to your XML file and the output CSV file
xml_path = "source/sdn_advanced.xml"
csv_file = "parsers/distinct_parties/dp_phase1.csv"
parse_distinct_party(xml_path, csv_file)
