import csv
from lxml import etree

# namespace and xpath build
namespace = {"ns": "http://www.un.org/sanctions/1.0"}


def parse_distinct_party(xml_path, csv_file):
    tree = etree.parse(xml_path)
    root = tree.getroot()

    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        header = [
            "DistinctPartyID",
            "ProfileID",
            "PartySubTypeID",
            "IdentityID",
            "AliasTypeID",
            "DocNameStatusID",
            "NameParts",
            "FeatureTypeID",
            "FeatureVersionReliabilityID",
            "FeatureVersionComment",
            "FeatureVersionLocationID",
            "DateOfBirth",
            "Address",
            "IDDetails",
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
                    alias_details = extract_alias_details(identity, namespace)
                    features = extract_features(profile, namespace)

                    writer.writerow(
                        [
                            distinct_party_id,
                            profile_id,
                            party_sub_type_id,
                            identity_id,
                            alias_details["AliasTypeID"],
                            alias_details["DocNameStatusID"],
                            alias_details["NameParts"],
                            features["FeatureTypeID"],
                            features["FeatureVersionLocationID"],
                            features["DateOfBirth"],
                        ]
                    )

    print(f"Data successfully written to {csv_file}")


def extract_alias_details(identity, namespace):
    alias_details = {"AliasTypeID": "", "DocNameStatusID": "", "NameParts": ""}
    for alias in identity.findall("ns:Alias", namespaces=namespace):
        alias_details["AliasTypeID"] = alias.get("AliasTypeID")
        documented_name = alias.find("ns:DocumentedName", namespaces=namespace)
        if documented_name is not None:
            alias_details["DocNameStatusID"] = documented_name.get("DocNameStatusID")
            name_parts = "; ".join(
                name_part.text
                for name_part in documented_name.findall(
                    "ns:DocumentedNamePart/ns:NamePartValue",
                    namespaces=namespace,
                )
            )
            alias_details["NameParts"] = name_parts
    return alias_details


def extract_features(profile, namespace):
    features = {
        "FeatureTypeID": "",
        "FeatureVersionLocationID": "",
        "DateOfBirth": "",
    }
    for feature in profile.findall("ns:Feature", namespaces=namespace):
        feature_type_id = feature.get("FeatureTypeID")
        for version in feature.findall("ns:FeatureVersion", namespaces=namespace):
            reliability_id = version.get("ReliabilityID")
            comment = version.findtext(
                "ns:Comment", namespaces=namespace, default="N/A"
            )
            location_element = version.find("ns:VersionLocation", namespaces=namespace)
            location_id = (
                location_element.get("LocationID")
                if location_element is not None
                else "N/A"
            )
            date_period = extract_date_period(version, namespace)

            if feature_type_id == "8":  # "8" is the FeatureTypeID for DOB
                features["DateOfBirth"] = date_period
            elif (
                feature_type_id == "9"
            ):  #  "9" is the FeatureTypeID for ( Place of Birth ) Address
                features["Address"] = comment
            elif feature_type_id == "10":  #  "10" is the FeatureTypeID for Nationality
                features["IDDetails"] = comment

            features["FeatureTypeID"] = feature_type_id
            features["FeatureVersionReliabilityID"] = reliability_id
            features["FeatureVersionComment"] = comment
            features["FeatureVersionLocationID"] = location_id
    return features


def extract_date_period(feature_version, namespace):
    date_period_element = feature_version.find("ns:DatePeriod", namespaces=namespace)
    if date_period_element is not None:
        start_element = date_period_element.find(
            "ns:Start/ns:From", namespaces=namespace
        )
        if start_element is not None:
            year = start_element.findtext("ns:Year", namespaces=namespace, default="")
            month = start_element.findtext("ns:Month", namespaces=namespace, default="")
            day = start_element.findtext("ns:Day", namespaces=namespace, default="")
            return f"{year}-{month}-{day}"
    return ""


xml_path = "source/sdn_advanced.xml"
csv_file = "custom_parsers/supplement/supplement_output.csv"
parse_distinct_party(xml_path, csv_file)
