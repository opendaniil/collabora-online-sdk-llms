---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/integrations/sharepoint.xhtml#configure-sharepoint"
source_file: "docs/integrations/sharepoint.xhtml"
source_anchor: "configure-sharepoint"
title: "Configure SharePoint"
canonical_title: "Integrations setup / SharePoint / Configure SharePoint"
toc_level: "2"
breadcrumbs: "Integrations setup / SharePoint / Configure SharePoint"
---
You need to configure WOPI bindings in SharePoint in order to associate actions to a WOPI application. The most common case it to associate all the document types to a single package, and in our case to Collabora Online.

Most of this will be done in the SharePoint Management Shell using PowerShell cmdlet. See [https://learn.microsoft.com/en-us/powershell/module/sharepointserver](https://learn.microsoft.com/en-us/powershell/module/sharepointserver) for an exhaustive documentation of the cmdlet. Carefully read the documentation as a lot of commands can change very important configuration. The following instructions are just a guidance and might have side effects on a setup that is more tailored to your need.

### Simple configuration: Always use Collabora Online

1. Clear the existing bindings. This is can be necessary as you can not have duplicated bindings.

> First, check the existing bindings with:
>
> ```
> Get-SPWOPIBinding
> ```
>
> If you have existing bindings, like if you already were using an existing installation of Office Online Server, and wanted to replace it completely you can remove all the binding:
>
> ```
> Remove-SPWOPIBinding -All
> ```
>
> See the documentation of [Remove-SPWOPIBinding](https://learn.microsoft.com/en-us/powershell/module/sharepoint-server/remove-spwopibinding?view=sharepoint-ps) [https://learn.microsoft.com/en-us/powershell/module/sharepoint-server/remove-spwopibinding?view=sharepoint-ps] for more details about that command and how just to remove them selectively.

2. Bind Collabora Online globally by just creating the binding:
  ```
  New-SPWOPIBinding -ServerName cool-server-name.example.com:port
  ```

> The default port for Collabora Online is 9980. Check your installation to determine if it is the same.
>
> Note
>
> Bindings can not be duplicated, so it might be necessary to clear the previous ones. See above.
>
> Note
>
> If you use Collabora Online in a testing environment without SSL, then you need to add `-AllowHTTP` to the command.

3. WOPI Zone

> It is necessary to set the WOPI Zone for Collabora Online. When running over https, Collabora Online uses `external-https` WOPI zone. So you need to set it:
>
> ```
> Set-SPWOPIZone -Zone "external-https"
> ```
>
> Note
>
> If you use Collabora Online in a testing environment without SSL, then the zone is `external-http`. However this is really not recommended.

### Advanced: Binding Collabora Online to a specific extension

If you want to use Collabora Online only selectively it is possible to have binding based on extensions.

For example, to use Collabora Online to open ODT files, run the command:

```
New-SPWOPIBinding -ServerName cool-server-name.example.com:port -Extension ODT
```

Execute this command for all the file extensions that you want to be handled by Collabora Online. The default port for Collabora Online is 9980. Check your installation to determine if it is the same.

Running this command requires that no binding exists for this extension in the external zone that Collabora Online uses.

### Default actions

Now SharePoint should use Collabora Online to open files with the configured extensions by default. Changing the default action for any of the configured file types can be done by using SharePoint’s [Get-SPWOPIBinding](https://learn.microsoft.com/en-us/powershell/module/sharepoint-server/get-spwopibinding) [https://learn.microsoft.com/en-us/powershell/module/sharepoint-server/get-spwopibinding] and [Set-SPWOPIBinding](https://learn.microsoft.com/en-us/powershell/module/sharepoint-server/set-spwopibinding) [https://learn.microsoft.com/en-us/powershell/module/sharepoint-server/set-spwopibinding] commands :

```
Get-SPWOPIBinding -Server cool-server-name.example.com:port -Extension ODT | Set-SPWOPIBinding -DefaultAction:$true
```
