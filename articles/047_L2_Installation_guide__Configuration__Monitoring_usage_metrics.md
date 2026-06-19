---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml#monitoring-usage-metrics"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: "monitoring-usage-metrics"
title: "Monitoring usage metrics"
canonical_title: "Installation guide / Configuration / Monitoring usage metrics"
toc_level: "2"
breadcrumbs: "Installation guide / Configuration / Monitoring usage metrics"
---
Collabora Online is capable of providing a wide variety of metrics related to system usage, eg. memory or CPU use, number of running kit processes or views in document sessions etc. The metrics can be retrieved in Prometheus-compatible format via the following URL:

```
https://*hostname*:*port*/cool/getMetrics
```

The URL uses the same authentication as the admin console. The available metrics are listed at: [https://github.com/CollaboraOnline/online/blob/main/wsd/metrics.txt](https://github.com/CollaboraOnline/online/blob/main/wsd/metrics.txt).

This requires admin_console to be enabled and the same condition as accessing the admin console or setting security.enable_metrics_unauthenticated to true.
