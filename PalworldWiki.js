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
                    `<link rel="stylesheet" href="http://localhost/css/${file}">`;
                $("head").append(result);
            });
            console.log("Removed Common.css link");
        }
    }

    for (const element of document.getElementsByClassName("mw-editsection")) {
        console.log("found", element);
        const children = element.getElementsByTagName("a");
        const visualEdit = children[0];
        const editSource = children[1];
        visualEdit.textContent = "Edit";
        editSource.textContent = "Edit Source";
        element.replaceChildren(visualEdit, editSource);
    }
})();