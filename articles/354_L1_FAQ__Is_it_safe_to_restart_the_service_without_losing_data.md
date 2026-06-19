---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/faq.xhtml#is-it-safe-to-restart-the-service-without-losing-data"
source_file: "docs/faq.xhtml"
source_anchor: "is-it-safe-to-restart-the-service-without-losing-data"
title: "Is it safe to restart the service without losing data?"
canonical_title: "FAQ / Is it safe to restart the service without losing data?"
toc_level: "1"
breadcrumbs: "FAQ / Is it safe to restart the service without losing data?"
---
Collabora Online is designed with data-safety first. When restarting the coolwsd service, the SIGINT signal is sent to the process. This initiates the shutdown procedure within coolwsd, which commences by flagging all documents to save and unload.

Each document that at that point has unsaved modifications would need to issue an internal save (much like auto-save) and, upon finishing the saving of the document successfully to disk, it will upload to Storage and, upon the successfully completion of uploading the document, it would unload it and disconnect all clients.

A message is typically displayed on the user’s clients (i.e. browser window) that the service is in maintenance and will return soon. The client logic tries to reconnect and reload the document at some interval and should automatically load the document and display it soon after coolwsd is back online.

Please note that restarting the coolwsd service has a maximum timeout (current defult is 120 seconds). If saving and uploading of a document does not finish within that timeout (f.e. due to network issues), the coolwsd process will be killed by systemd as it would have exceeded its maximum shutdown timeout. This could result in data-loss, unless the Quarantine feature is enabled and the document had been saved to disk by that point.

The service shutdown-timeout can be changed through systemd configuration (the entry in question is TimeoutStopSec under [Service]).

Note that coolwsd has a forced-shutdown mode. If multiple SIGINT (or SIGTERM) signals are sent, the process will not wait for the documents to save, upload, and unload, but will exit promptly. This is normally not necessary and not recommended as it will not wait until the completion of document save and upload, resulting in data loss.
