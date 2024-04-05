import csv
from lxml import etree

# Load the XML content. Replace 'path_to_your_file.xml' with the actual file path
xml_path = "source/sdn_advanced.xml"
tree = etree.parse(xml_path)
root = tree.getroot()

# Define the namespace
ns = {"ns": "http://www.un.org/sanctions/1.0"}


# Function to write data to CSV
def write_to_csv(file_name, header, rows):
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


# Parse AliasTypeValues
alias_types = []
for alias_type in root.findall(".//ns:AliasTypeValues/ns:AliasType", ns):
    id_value = alias_type.get("ID")
    description = alias_type.text
    alias_types.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/alias_type_values.csv",
    ["ID", "Description"],
    alias_types,
)

# Parse AreaCodeValues
area_codes = []
for area_code in root.findall(".//ns:AreaCodeValues/ns:AreaCode", ns):
    id_value = area_code.get("ID")
    country_id = area_code.get("CountryID")
    description = area_code.get("Description")
    area_code_type_id = area_code.get("AreaCodeTypeID")
    shorthand = area_code.text
    area_codes.append([id_value, country_id, description, area_code_type_id, shorthand])
write_to_csv(
    "parsers/reference_value_sets/area_code_values.csv",
    ["ID", "CountryID", "Description", "AreaCodeTypeID", "Shorthand"],
    area_codes,
)

# Parse CountryValues
countries = []
for country in root.findall(".//ns:CountryValues/ns:Country", ns):
    id_value = country.get("ID")
    iso2 = country.get("ISO2")
    description = country.text
    countries.append([id_value, iso2, description])
write_to_csv(
    "parsers/reference_value_sets/country_values.csv",
    ["ID", "ISO2", "Description"],
    countries,
)

print("Data successfully written to separate CSV files.")

# <!-- parse 3 : ignore but done -->
# <AreaCodeTypeValues>
#   <AreaCodeType ID="1">ISO 3166 (2)</AreaCodeType>
# </AreaCodeTypeValues>

# <!-- parse 4 : ignore but done -->
# <CalendarTypeValues>
#   <CalendarType ID="1">Gregorian</CalendarType>
# </CalendarTypeValues>

# Parse AreaCodeTypeValues
area_code_types = []
for area_code_type in root.findall(".//ns:AreaCodeTypeValues/ns:AreaCodeType", ns):
    id_value = area_code_type.get("ID")
    description = area_code_type.text
    area_code_types.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/area_code_type_values.csv",
    ["ID", "Description"],
    area_code_types,
)

# Parse CalendarTypeValues
calendar_types = []
for calendar_type in root.findall(".//ns:CalendarTypeValues/ns:CalendarType", ns):
    id_value = calendar_type.get("ID")
    description = calendar_type.text
    calendar_types.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/calendar_type_values.csv",
    ["ID", "Description"],
    calendar_types,
)


# Parse CountryRelevanceValues
country_relevance_values = []
for country_relevance in root.findall(
    ".//ns:CountryRelevanceValues/ns:CountryRelevance", ns
):
    id_value = country_relevance.get("ID")
    description = country_relevance.text
    country_relevance_values.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/country_relevance_values.csv",
    ["ID", "Description"],
    country_relevance_values,
)

# Parse DecisionMakingBodyValues
decision_making_body_values = []
for decision_making_body in root.findall(
    ".//ns:DecisionMakingBodyValues/ns:DecisionMakingBody", ns
):
    id_value = decision_making_body.get("ID")
    organisation_id = decision_making_body.get("OrganisationID")
    description = decision_making_body.text
    decision_making_body_values.append([id_value, organisation_id, description])
write_to_csv(
    "parsers/reference_value_sets/decision_making_body_values.csv",
    ["ID", "OrganisationID", "Description"],
    decision_making_body_values,
)

# !

# Parse DetailReferenceValues
detail_references = []
for detail_reference in root.findall(
    ".//ns:DetailReferenceValues/ns:DetailReference", ns
):
    id_value = detail_reference.get("ID")
    description = detail_reference.text
    detail_references.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/detail_reference_values.csv",
    ["ID", "Description"],
    detail_references,
)

# Parse DetailTypeValues
detail_types = []
for detail_type in root.findall(".//ns:DetailTypeValues/ns:DetailType", ns):
    id_value = detail_type.get("ID")
    description = detail_type.text
    detail_types.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/detail_type_values.csv",
    ["ID", "Description"],
    detail_types,
)

# Parse DocNameStatusValues
doc_name_statuses = []
for doc_name_status in root.findall(".//ns:DocNameStatusValues/ns:DocNameStatus", ns):
    id_value = doc_name_status.get("ID")
    description = doc_name_status.text
    doc_name_statuses.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/doc_name_status_values.csv",
    ["ID", "Description"],
    doc_name_statuses,
)

# Parse EntryEventTypeValues
entry_event_types = []
for entry_event_type in root.findall(
    ".//ns:EntryEventTypeValues/ns:EntryEventType", ns
):
    id_value = entry_event_type.get("ID")
    description = entry_event_type.text
    entry_event_types.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/entry_event_type_values.csv",
    ["ID", "Description"],
    entry_event_types,
)


# !

# Parse FeatureTypeValues
feature_types = []
for feature_type in root.findall(".//ns:FeatureTypeValues/ns:FeatureType", ns):
    id_value = feature_type.get("ID")
    group_id = feature_type.get("FeatureTypeGroupID")
    description = feature_type.text
    feature_types.append([id_value, group_id, description])
write_to_csv(
    "parsers/reference_value_sets/feature_type_values.csv",
    ["ID", "FeatureTypeGroupID", "Description"],
    feature_types,
)

# Parse FeatureTypeGroupValues
feature_type_groups = []
for feature_type_group in root.findall(
    ".//ns:FeatureTypeGroupValues/ns:FeatureTypeGroup", ns
):
    id_value = feature_type_group.get("ID")
    description = feature_type_group.text
    feature_type_groups.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/feature_type_group_values.csv",
    ["ID", "Description"],
    feature_type_groups,
)

# Parse IDRegDocDateTypeValues
id_reg_doc_date_types = []
for id_reg_doc_date_type in root.findall(
    ".//ns:IDRegDocDateTypeValues/ns:IDRegDocDateType", ns
):
    id_value = id_reg_doc_date_type.get("ID")
    description = id_reg_doc_date_type.text
    id_reg_doc_date_types.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/id_reg_doc_date_type_values.csv",
    ["ID", "Description"],
    id_reg_doc_date_types,
)

# Parse IDRegDocTypeValues
id_reg_doc_types = []
for id_reg_doc_type in root.findall(".//ns:IDRegDocTypeValues/ns:IDRegDocType", ns):
    id_value = id_reg_doc_type.get("ID")
    description = id_reg_doc_type.text
    id_reg_doc_types.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/id_reg_doc_type_values.csv",
    ["ID", "Description"],
    id_reg_doc_types,
)

# !!! importan

# Parse LegalBasisValues
legal_basis_values = []
for legal_basis in root.findall(".//ns:LegalBasisValues/ns:LegalBasis", ns):
    id_value = legal_basis.get("ID")
    short_ref = legal_basis.get("LegalBasisShortRef")
    type_id = legal_basis.get("LegalBasisTypeID")
    program_id = legal_basis.get("SanctionsProgramID")
    description = legal_basis.text
    legal_basis_values.append([id_value, short_ref, type_id, program_id, description])
write_to_csv(
    "parsers/reference_value_sets/legal_basis_values.csv",
    [
        "ID",
        "LegalBasisShortRef",
        "LegalBasisTypeID",
        "SanctionsProgramID",
        "Description",
    ],
    legal_basis_values,
)

# Parse LegalBasisTypeValues
legal_basis_type_values = []
for legal_basis_type in root.findall(
    ".//ns:LegalBasisTypeValues/ns:LegalBasisType", ns
):
    id_value = legal_basis_type.get("ID")
    description = legal_basis_type.text
    legal_basis_type_values.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/legal_basis_type_values.csv",
    ["ID", "Description"],
    legal_basis_type_values,
)

# !


# Parse ListValues
list_values = []
for list_value in root.findall(".//ns:ListValues/ns:List", ns):
    id_value = list_value.get("ID")
    description = list_value.text
    list_values.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/list_values.csv", ["ID", "Description"], list_values
)

# Parse LocPartTypeValues
loc_part_types = []
for loc_part_type in root.findall(".//ns:LocPartTypeValues/ns:LocPartType", ns):
    id_value = loc_part_type.get("ID")
    description = loc_part_type.text
    loc_part_types.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/loc_part_type_values.csv",
    ["ID", "Description"],
    loc_part_types,
)

# Parse LocPartValueStatusValues
loc_part_value_statuses = []
for loc_part_value_status in root.findall(
    ".//ns:LocPartValueStatusValues/ns:LocPartValueStatus", ns
):
    id_value = loc_part_value_status.get("ID")
    description = loc_part_value_status.text
    loc_part_value_statuses.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/loc_part_value_status_values.csv",
    ["ID", "Description"],
    loc_part_value_statuses,
)

# !

# Parse NamePartTypeValues
name_part_types = []
for name_part_type in root.findall(".//ns:NamePartTypeValues/ns:NamePartType", ns):
    id_value = name_part_type.get("ID")
    description = name_part_type.text
    name_part_types.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/name_part_type_values.csv",
    ["ID", "Description"],
    name_part_types,
)


# Parse OrganisationValues
organisations = []
for organisation in root.findall(".//ns:OrganisationValues/ns:Organisation", ns):
    id_value = organisation.get("ID")
    country_id = organisation.get("CountryID")
    description = organisation.text
    organisations.append([id_value, country_id, description])
write_to_csv(
    "parsers/reference_value_sets/organisation_values.csv",
    ["ID", "CountryID", "Description"],
    organisations,
)

# Parse PartySubTypeValues
party_sub_types = []
for party_sub_type in root.findall(".//ns:PartySubTypeValues/ns:PartySubType", ns):
    id_value = party_sub_type.get("ID")
    party_type_id = party_sub_type.get("PartyTypeID")
    description = party_sub_type.text
    party_sub_types.append([id_value, party_type_id, description])
write_to_csv(
    "parsers/reference_value_sets/party_sub_type_values.csv",
    ["ID", "PartyTypeID", "Description"],
    party_sub_types,
)

# Parse PartyTypeValues
party_types = []
for party_type in root.findall(".//ns:PartyTypeValues/ns:PartyType", ns):
    id_value = party_type.get("ID")
    description = party_type.text
    party_types.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/party_type_values.csv",
    ["ID", "Description"],
    party_types,
)

# !
# Parse RelationQualityValues
relation_quality_values = []
for relation_quality in root.findall(
    ".//ns:RelationQualityValues/ns:RelationQuality", ns
):
    id_value = relation_quality.get("ID")
    description = relation_quality.text
    relation_quality_values.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/relation_quality_values.csv",
    ["ID", "Description"],
    relation_quality_values,
)

# Parse RelationTypeValues
relation_type_values = []
for relation_type in root.findall(".//ns:RelationTypeValues/ns:RelationType", ns):
    id_value = relation_type.get("ID")
    symmetrical = relation_type.get("Symmetrical")
    description = relation_type.text
    relation_type_values.append([id_value, symmetrical, description])
write_to_csv(
    "parsers/reference_value_sets/relation_type_values.csv",
    ["ID", "Symmetrical", "Description"],
    relation_type_values,
)

# Parse ReliabilityValues
reliability_values = []
for reliability in root.findall(".//ns:ReliabilityValues/ns:Reliability", ns):
    id_value = reliability.get("ID")
    description = reliability.text
    reliability_values.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/reliability_values.csv",
    ["ID", "Description"],
    reliability_values,
)


# !

# Parse SanctionsProgramValues
sanctions_programs = []
for sanctions_program in root.findall(
    ".//ns:SanctionsProgramValues/ns:SanctionsProgram", ns
):
    id_value = sanctions_program.get("ID")
    subsidiary_body_id = sanctions_program.get("SubsidiaryBodyID")
    description = sanctions_program.text
    sanctions_programs.append([id_value, subsidiary_body_id, description])
write_to_csv(
    "parsers/reference_value_sets/sanctions_program_values.csv",
    ["ID", "SubsidiaryBodyID", "Description"],
    sanctions_programs,
)

# Parse SanctionsTypeValues
sanctions_types = []
for sanctions_type in root.findall(".//ns:SanctionsTypeValues/ns:SanctionsType", ns):
    id_value = sanctions_type.get("ID")
    description = sanctions_type.text
    sanctions_types.append([id_value, description])
write_to_csv(
    "parsers/reference_value_sets/sanctions_type_values.csv",
    ["ID", "Description"],
    sanctions_types,
)

# Parse ScriptValues
scripts = []
for script in root.findall(".//ns:ScriptValues/ns:Script", ns):
    id_value = script.get("ID")
    script_code = script.get("ScriptCode")
    description = script.text
    scripts.append([id_value, script_code, description])
write_to_csv(
    "parsers/reference_value_sets/script_values.csv",
    ["ID", "ScriptCode", "Description"],
    scripts,
)
