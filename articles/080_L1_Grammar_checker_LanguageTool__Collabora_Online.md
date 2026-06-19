---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/language_tool.xhtml#collabora-online"
source_file: "docs/language_tool.xhtml"
source_anchor: "collabora-online"
title: "Collabora Online"
canonical_title: "Grammar checker (LanguageTool) / Collabora Online"
toc_level: "1"
breadcrumbs: "Grammar checker (LanguageTool) / Collabora Online"
---
You can find the respective option within your coolwsd.xml where you can set the LanguageTool.org API settings you need within the languagetool block. To turn it on, please set “enabled” property to true. The base URL may be https://api.languagetoolplus.com/v2 if the cloud version is used. However, your data in the document e.g. the text part of it will be sent to the cloud API. Please read the privacy policy: [https://languagetool.org/legal/privacy](https://languagetool.org/legal/privacy).

Languagetool block of coolwsd.xml

```
 <languagetool desc="LanguageTool Remote API settings for grammar checking">
     <enabled desc="Enable LanguageTool Remote Grammar Checker" type="bool" default="false">true</enabled>
     <base_url desc="Http endpoint for the LanguageTool API server, without /check or /languages postfix at the end." type="string" default="">https://api.languagetoolplus.com/v2</base_url>
     <user_name desc="LangueTool account username for premium usage." type="string" default=""></user_name>
     <api_key desc="Api key provided by LanguageTool account for premium usage." type="string" default=""></api_key>
</languagetool>
```

Please note, LanguageTool plugin uses `libcurl and thus the base_url has to have http:// or https:// as the prefix. Currently, the expected URL scheme should include the API version (as stated in [LanguageTool API](https://languagetool.org/http-api/) [https://languagetool.org/http-api/]). E.g.: https://selfhostedlg.com/v2

Free and paid versions (including on-premise premium version) are available from [LanguageTool](https://languagetool.org/premium?a=collabora) [https://languagetool.org/premium?a=collabora].
