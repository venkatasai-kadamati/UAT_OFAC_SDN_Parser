import csv
from lxml import etree

namespace = {"ns": "http://www.un.org/sanctions/1.0"}

# loading target xml
xml_path = "source/sdn_advanced.xml"
tree = etree.parse(xml_path)
root = tree.getroot()

# csv writer
csv_file = "parsers/profile_relationships/profile_relationships.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "ID",
            "From-ProfileID",
            "To-ProfileID",
            "RelationTypeID",
            "RelationQualityID",
            "Former",
            "SanctionsEntryID",
            "Comment",
        ]
    )

    # Iterate over each ProfileRelationship element
    for profile_relationship in root.findall(
        "ns:ProfileRelationships/ns:ProfileRelationship", namespaces=namespace
    ):
        id_value = profile_relationship.get("ID")
        from_profile_id = profile_relationship.get("From-ProfileID")
        to_profile_id = profile_relationship.get("To-ProfileID")
        relation_type_id = profile_relationship.get("RelationTypeID")
        relation_quality_id = profile_relationship.get("RelationQualityID")
        former = profile_relationship.get("Former")
        sanctions_entry_id = profile_relationship.get("SanctionsEntryID")
        comment = profile_relationship.findtext(
            "ns:Comment", namespaces=namespace, default=""
        )

        writer.writerow(
            [
                id_value,
                from_profile_id,
                to_profile_id,
                relation_type_id,
                relation_quality_id,
                former,
                sanctions_entry_id,
                comment,
            ]
        )

print(f"Data successfully written to {csv_file}")
