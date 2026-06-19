---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml"
source_file: "docs/postmessage_api.xhtml"
source_anchor: ""
title: "PostMessage API"
canonical_title: "PostMessage API"
toc_level: "0"
breadcrumbs: "PostMessage API"
---
PostMessage API is used to interact with parent frame when Collabora Online’s browser part is enclosed in one. This is useful for hosts wanting to integrate Collabora Online in them.

This API is mostly based on [WOPI specification](https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/online/scenarios/postmessage) [https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/online/scenarios/postmessage] with few extensions/modifications. All messages sent are in this form :

```
{
    "MessageId": "<MessageId>",
    "SendTime": "<Timestamp when message is sent>",
    "Values": {
         "<key>": "<value>"
    }
}
```

`SendTime` is the timestamp returned by browsers’ Date.now(). The post messages sent from the WOPI host should also be in same form.

It is to be noted that as mentioned in WOPI specs, Collabora Online frame will ignore all post messages coming from the host frame if Host_PostmessageReady has not been received. Further, since for embedding Collabora Online as an iframe WOPI implementation is a must, it is required that `PostMessageOrigin` property is present in WOPI host’s CheckFileInfo response. Otherwise, no post messages will be emitted.
