(function () {
    'use strict';
    const CSSFiles = [
        "root.css",
        "headings.css",
        "ads.css",
        "diff.css",
        "images.css",
        "keyframes.css",
        "links.css",
        "localization.css",
        "main-page.css",
        "media.css",
        "mw-echo.css",
        "navigation.css",
        "oo-ui.css",
        "portable-infobox.css",
        "source-editor.css",
        "tabber.css",
        "tables.css",
        "toc.css",
        "video.css",
        "visual-editor.css",
        "wiki-templates.css",
    ];

    for (const linkElement of document.getElementsByTagName("link")) {
        if (linkElement.href.endsWith("/load.php?lang=en&modules=site.styles&only=styles&skin=vector")) {
            linkElement.remove();
            CSSFiles.forEach(function (file) {
                const result =
                    `<link rel="stylesheet" href="http://192.168.0.18/css/${file}">`;
                $("head").append(result);
            });
            console.log("Removed Common.css link");
        }
    }
    const ViewHistoryTab = $("#ca-history");
    const WatchTab = $("#ca-watch");
    const MoreTabList = $("#p-cactions ul");
    const RightNavigation = $("#p-views div");

    const TabsMediaQuery = window.matchMedia('(max-width: 800px)');
    TabsMediaQuery.onchange = (query) => {
        if (query.matches) {
            console.log("owo");
            ViewHistoryTab.appendTo(MoreTabList)
            WatchTab.appendTo(MoreTabList)

        }
        else {
            ViewHistoryTab.appendTo(RightNavigation)
            WatchTab.appendTo(RightNavigation)
        }
    }
    TabsMediaQuery.onchange(TabsMediaQuery);

})();