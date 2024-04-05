import csv
from lxml import etree

# Define the namespace map based on the XML structure.
namespace = {"ns": "http://www.un.org/sanctions/1.0"}


def parse_features(xml_path, csv_file):
    tree = etree.parse(xml_path)
    root = tree.getroot()

    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "DistinctPartyID",
                "ProfileID",
                "FeatureID",
                "FeatureTypeID",
                "FeatureVersionReliabilityID",
                "FeatureVersionComment",
                "FeatureVersionLocationID",
                "DatePeriodDetails",
            ]
        )

        for distinct_party in root.findall(
            "ns:DistinctParties/ns:DistinctParty", namespaces=namespace
        ):
            distinct_party_id = distinct_party.get("FixedRef")
            for profile in distinct_party.findall("ns:Profile", namespaces=namespace):
                profile_id = profile.get("ID")
                for feature in profile.findall("ns:Feature", namespaces=namespace):
                    feature_id = feature.get("ID")
                    feature_type_id = feature.get("FeatureTypeID")
                    for version in feature.findall(
                        "ns:FeatureVersion", namespaces=namespace
                    ):
                        reliability_id = version.get("ReliabilityID")
                        comment = version.findtext(
                            "ns:Comment", namespaces=namespace, default="N/A"
                        )
                        location_id = (
                            version.find(
                                "ns:VersionLocation", namespaces=namespace
                            ).get("LocationID", "N/A")
                            if version.find("ns:VersionLocation", namespaces=namespace)
                            is not None
                            else "N/A"
                        )
                        date_period_details = extract_date_period(version)
                        writer.writerow(
                            [
                                distinct_party_id,
                                profile_id,
                                feature_id,
                                feature_type_id,
                                reliability_id,
                                comment,
                                location_id,
                                date_period_details,
                            ]
                        )

    print(f"Data successfully written to {csv_file}")


def extract_date_period(feature_version):
    date_period = feature_version.find("ns:DatePeriod", namespaces=namespace)
    if date_period is not None:
        start = date_period.find("ns:Start", namespaces=namespace)
        end = date_period.find("ns:End", namespaces=namespace)
        start_date = f"{start.findtext('ns:From/ns:Year', namespaces=namespace)}-{start.findtext('ns:From/ns:Month', namespaces=namespace)}-{start.findtext('ns:From/ns:Day', namespaces=namespace)}"
        end_date = f"{end.findtext('ns:To/ns:Year', namespaces=namespace)}-{end.findtext('ns:To/ns:Month', namespaces=namespace)}-{end.findtext('ns:To/ns:Day', namespaces=namespace)}"
        return f"Start: {start_date}, End: {end_date}"
    return "N/A"


parse_features(
    "source/sdn_advanced.xml", "parsers/distinct_parties/features_details.csv"
)
