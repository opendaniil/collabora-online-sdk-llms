---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/Step_by_step_tutorial.xhtml"
source_file: "docs/Step_by_step_tutorial.xhtml"
source_anchor: ""
title: "Step-by-step tutorial"
canonical_title: "Step-by-step tutorial"
toc_level: "0"
breadcrumbs: "Step-by-step tutorial"
---
It is not practical trying to implement everything in one go. We recommend building the integration in small, easily testable steps, like the following:

1. Install Collabora Online on a dedicated server or in a VM, and make sure you can access the discovery service by pointing your browser to
  ```
  https://<WOPI client URL>:<port>/hosting/discovery
  ```
2. Add WOPI REST endpoints to your web service, for the moment returning only a “Hello World” message upon a GET request, that you can evaluate via a web browser. If you need, you can for example use Apache’s mod_rewrite so that the REST endpoints are redirected to URL of your choice. At this moment, test that
  ```
  https://<WOPI host URL>/<...>/wopi/files/<id>/contents
  ```
  returns Hello World for whatever `<id>`.
3. Implement the CheckFileInfo endpoint – make sure that
  ```
  https://<WOPI host URL>/<...>/wopi/files/<id>
  ```
  returns JSON like `{ "BaseFileName": "test.txt", "Size": 11 }`
4. At this moment, you will be able to see a constructed document in Collabora Online: Create a URL by concatenating URL from the discovery XML (see the point 1), and add `WOPISrc=https://<WOPI host URL>/<...>/wopi/files/<id>` at the end, resulting in URL like
  ```
  https://<WOPI client URL>:<port>/browser/<hash>/cool.html?WOPISrc=https://<WOPI host URL>/<...>/wopi/files/<id>
  ```

> Create a small test.html file containing:
>
> ```
>  1<!DOCTYPE html>
>  2<html>
>  3<head>
>  4    <meta charset="utf-8"/>
>  5    <meta name="viewport" content="width=device-width, initial-scale=1"/>
>  6    <title>Load Collabora Online</title>
>  7</head>
>  8<body>
>  9    <form action="...URL you constructed..." enctype="multipart/form-data" method="post">
> 10        <input name="access_token" value="test" type="hidden"/>
> 11        <input type="submit" value="Load Collabora Online"/>
> 12    </form>
> 13</body>
> 14</html>
> ```
>
> Note
>
> The `<meta name="viewport" content="width=device-width, initial-scale=1">` line in the `<head>` is essential for a correct mobile experience. Without it, mobile browsers fall back to a desktop emulation width (around 980 CSS pixels in Chrome on Android) and scale the whole page down to fit the device. The embedded Collabora Online iframe is scaled down with it, producing a miniature UI with hit targets too small to tap. Inside the iframe, `window.innerWidth` reports the parent’s desktop-emulated width rather than the device’s actual width, so Collabora Online loads its desktop interface instead of the touch-optimised mobile one.
>
> Do not append `user-scalable=no` or `maximum-scale=1` to the `content` attribute: those break pinch-to-zoom for low-vision users (WCAG SC 1.4.4) without solving anything.
>
> For the underlying mechanism, see [MDN’s Viewport meta tag page](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport) [https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport] and the [Lighthouse ‘viewport’ audit](https://developer.chrome.com/docs/lighthouse/best-practices/viewport) [https://developer.chrome.com/docs/lighthouse/best-practices/viewport].
>
> When you load it in the browser and click the **Load Collabora Online** button, it will open a text document that shows “Hello World” provided by the WOPI endpoints. If your WOPI host is on a different machine than Collabora’s, make sure to add that host along with the port in the configuration file coolwsd.xml under `<storage>` → `<wopi>` tag.

5. From this point, you have the basics working, and you have to extend the JavaScript pieces: Create an iframe that will contain the Collabora Online, and provide that with a real access token. From the Collabora Online point of view, the access token can be any random text or number that contains just numbers, characters, and underlines.
6. Update your REST endpoints so that they provide real data instead of a synthesized “Hello World” and hard-coded document length.
7. Implement the PutFile end point, so that the results of editing can appear in your file storage too. To do this, implement the POST request to
  ```
  https://<WOPI host URL>/<...>/wopi/files/<id>/contents
  ```
8. Either implement the PutRelativeFile endpoint, so that the option to Save As appears in the UI, or change CheckFileInfo to return **UserCanNotWriteRelative** with value **true** if you don’t want to do that yet.
