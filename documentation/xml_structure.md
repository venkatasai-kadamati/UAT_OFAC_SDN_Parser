1. Distinct Parties

```(sql)
DistinctParty
└── Profile
    ├── Identity
    │   ├── Alias
    │   │   └── DocumentedName
    │   │       └── DocumentedNamePart
    │   │           └── NamePartValue
    │   ├── Alias
    │   │   └── DocumentedName
    │   │       └── DocumentedNamePart
    │   │           └── NamePartValue
    │   └── NamePartGroups
    │       ├── MasterNamePartGroup
    │       │   └── NamePartGroup
    │       └── MasterNamePartGroup
    │           └── NamePartGroup
    └── Feature
        ├── FeatureVersion
        │   └── VersionLocation
        └── IdentityReference
```

## Solution: Mapping the elements/ attributes with the codebase

• DistinctParty node (1 attribute):
• @FixedRef attribute: Parsed and stored in data['FixedRef'].
• Comment node (1 attribute):
• Text content: Parsed and stored in data['Comment'].
• Profile node (2 attributes):
• @ID attribute: Parsed and stored in data['ProfileID'].
• @PartySubTypeID attribute: Parsed and stored in data['PartySubTypeID'].
• Identity node (4 attributes):
• @ID attribute: Parsed and stored in data['IdentityID'].
• @FixedRef attribute: Parsed and stored in data['IdentityFixedRef'].
• @Primary attribute: Parsed and stored in data['IdentityPrimary'].
• @False attribute: Parsed and stored in data['IdentityFalse'].
• Alias node (4 attributes):
• @FixedRef attribute: Parsed and stored in alias_data['AliasFixedRef'].
• @AliasTypeID attribute: Parsed and stored in alias_data['AliasTypeID'].
• @Primary attribute: Parsed and stored in alias_data['AliasPrimary'].
• @LowQuality attribute: Parsed and stored in alias_data['AliasLowQuality'].
• DocumentedName node (3 attributes):
• @ID attribute: Parsed and stored in alias_data['DocNameID'].
• @FixedRef attribute: Parsed and stored in alias_data['DocNameFixedRef'].
• @DocNameStatusID attribute: Parsed and stored in alias_data['DocNameStatusID'].
• DocumentedNamePart node (1 attribute):
• NamePartValue node (4 attributes):
• Text content: Parsed and stored in alias_data['NamePartValue'].
• @NamePartGroupID attribute: Parsed and stored in alias_data['NamePartGroupID'].
• @ScriptID attribute: Parsed and stored in alias_data['ScriptID'].
• @ScriptStatusID attribute: Parsed and stored in alias_data['ScriptStatusID'].
@Acronym attribute: Parsed and stored in alias_data['Acronym'].

- Total entries of unique distinct party : 48200
  <DistinctParty FixedRef="48200">

<!-- Location -->

## Breakdown of 'Locations' XML Document

1. Locations node with no attributes.

2. Location node with 1 attribute:
   • @ID attribute.
3. LocationAreaCode node with 1 attribute:
   • @AreaCodeID attribute.

4. LocationCountry node with 2 attributes:
   • @CountryID attribute.
   • @CountryRelevanceID attribute.
5. LocationPart node with 1 attribute:
   • @LocPartTypeID attribute.
   • LocationPartValue node with 3 attributes:
   ○ @Primary attribute.
   ○ @LocPartValueTypeID attribute.
   ○ @LocPartValueStatusID attribute.
   • Comment node with no attributes.
   • Value node with no attributes.

6. FeatureVersionReference node with 1 attribute:
   • @FeatureVersionID attribute.

To sum up :
• Nodes: 6 (excluding repeated nodes and Comment and Value nodes as they do not have attributes and are not unique)
• Attributes: 9
• Total count: 15

<!-- Referencevalueset -->

## Breakdown of 'ReferenceValueSets' XML Document

1. ReferenceValueSets node with no attributes.
2. AliasTypeValues node with no attributes.
   • AliasType node with 1 attribute:
   • @ID attribute.

3. AreaCodeValues node with no attributes.
   • AreaCode node with 4 attributes:
   • @ID attribute.
   • @CountryID attribute.
   • @Description attribute.
   • @AreaCodeTypeID attribute.

4. AreaCodeTypeValues node with no attributes.
   • AreaCodeType node with 1 attribute:
   • @ID attribute.

5. CalendarTypeValues node with no attributes.
   • CalendarType node with 1 attribute:
   • @ID attribute.

6. CountryValues node with no attributes.
   • Country node with 2 attributes:
   • @ID attribute.
   • @ISO2 attribute.

7. CountryRelevanceValues node with no attributes.
   • CountryRelevance node with 1 attribute:
   • @ID attribute.

8. DecisionMakingBodyValues node with no attributes.
   • DecisionMakingBody node with 2 attributes:
   • @ID attribute.
   • @OrganisationID attribute.

9. DetailReferenceValues node with no attributes.
   • DetailReference node with 1 attribute:
   • @ID attribute.

10. DetailTypeValues node with no attributes.
    • DetailType node with 1 attribute:
    • @ID attribute.

11. DocNameStatusValues node with no attributes.
    • DocNameStatus node with 1 attribute:
    • @ID attribute.

12. EntryEventTypeValues node with no attributes.
    • EntryEventType node with 1 attribute:
    • @ID attribute.

13. FeatureTypeValues node with no attributes.
    • FeatureType node with 3 attributes:
    • @ID attribute.
    • @FeatureTypeGroupID attribute.
    • @Secondary sanctions risk attribute (implied from context, not directly stated).

14. FeatureTypeGroupValues node with no attributes.
    • FeatureTypeGroup node with 1 attribute:
    • @ID attribute.

15. IDRegDocDateTypeValues node with no attributes.
    • IDRegDocDateType node with 1 attribute:
    • @ID attribute.

16. IDRegDocTypeValues node with no attributes.
    • IDRegDocType node with 1 attribute:
    • @ID attribute.

17. IdentityFeatureLinkTypeValues node with no attributes.
    • IdentityFeatureLinkType node with 1 attribute:
    • @ID attribute.

18. LegalBasisValues node with no attributes.
    • LegalBasis node with 4 attributes:
    • @ID attribute.
    • @LegalBasisShortRef attribute.
    • @LegalBasisTypeID attribute.
    • @SanctionsProgramID attribute.

19. LegalBasisTypeValues node with no attributes.
    • LegalBasisType node with 1 attribute:
    • @ID attribute.

20. ListValues node with no attributes.
    • List node with 1 attribute:
    • @ID attribute.

21. LocPartTypeValues node with no attributes.
    • LocPartType node with 1 attribute:
    • @ID attribute.

22. LocPartValueStatusValues node with no attributes.
    • LocPartValueStatus node with 1 attribute:
    • @ID attribute.

23. LocPartValueTypeValues node with no attributes.
    • LocPartValueType node with 1 attribute:
    • @ID attribute.

24. NamePartTypeValues node with no attributes.
    • NamePartType node with 1 attribute:
    • @ID attribute.

25. OrganisationValues node with no attributes.
    • Organisation node with 1 attribute:
    • @ID attribute.

26. PartySubTypeValues node with no attributes.
    • PartySubType node with 2 attributes:
    • @ID attribute.
    • @PartyTypeID attribute.

27. PartyTypeValues node with no attributes.
    • PartyType node with 1 attribute:
    • @ID attribute.

28. RelationQualityValues node with no attributes.
    • RelationQuality node with 1 attribute:
    • @ID attribute.

29. RelationTypeValues node with no attributes.
    • RelationType node with 2 attributes:
    • @ID attribute.
    • @Symmetrical attribute.

30. ReliabilityValues node with no attributes.
    • Reliability node with 1 attribute:
    • @ID attribute.

31. SanctionsProgramValues node with no attributes.
    • SanctionsProgram node with 2 attributes:
    • @ID attribute.
    • @SubsidiaryBodyID attribute.

32. SanctionsTypeValues node with no attributes.
    • SanctionsType node with 1 attribute:
    • @ID attribute.

33. ScriptValues node with no attributes.
    • Script node with 2 attributes:
    • @ID attribute.
    • @ScriptCode attribute.

34. ScriptStatusValues node with no attributes.
    • ScriptStatus node with 1 attribute:
    • @ID attribute.

35. SubsidiaryBodyValues node with no attributes.
    • SubsidiaryBody node with 2 attributes:
    • @ID attribute.
    • @DecisionMakingBodyID attribute.

36. SupInfoTypeValues node with no attributes.
37. TargetTypeValues node with no attributes.
38. ValidityValues node with no attributes.
    • Validity node with 1 attribute:
    • @ID attribute.

To sum up:
• Nodes: 38 (excluding repeated nodes and nodes without attributes)
• Attributes: Numerous, with some nodes having multiple attributes.
