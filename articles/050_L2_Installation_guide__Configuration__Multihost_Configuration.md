---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml#multihost-configuration"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: "multihost-configuration"
title: "Multihost Configuration"
canonical_title: "Installation guide / Configuration / Multihost Configuration"
toc_level: "2"
breadcrumbs: "Installation guide / Configuration / Multihost Configuration"
---
To use multiple host and aliases with one COOL server you have to set alias_groups mode attribute to ‘groups’ and define group for each intergrator’s instance.

```
<alias_groups desc="default mode is 'first' it allows only the first host when groups are not defined. set mode to 'groups' and define group to allow multiple host and its aliases" mode="groups">
<!-- If you need to use multiple wopi hosts, please change the mode to "groups" and
add the hosts below.  If one host is accessible under multiple ip addresses
or names, add them as aliases. -->

   <group>
      <host desc="hostname to allow or deny." allow="true">https://host1:443</host>
   </group>

   <group>
      <host desc="hostname to allow or deny." allow="true">https://host2:443</host>
      <alias desc="regex pattern of aliasname">https://aliasname[0-9]{1}:443</alias>
   </group>

   <!-- More "group"s possible here -->
</alias_groups>
```

You can add multiple groups. Here host1 and host2 can be any service COOL has integration with [Available integrations](084_L0_Available_integrations.md).
