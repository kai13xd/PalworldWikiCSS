from glob import glob
import tinycss2 as tcss
import os

def IsComment(node):
    if node.type == 'comment':
        return True
    elif node.type == 'whitespace':
        node.value = '\n'
    elif node.type == 'qualified-rule':
        node.content = [node for node in node.content if not IsComment(node)]
    else:
        print(node.type)
    return False


def AddCommentNode(*comment:str):
    result = "\n\t".join(comment)
    result = f"{"="*96}\n\t{result}\n{"="*96}"
    return tcss.tokenizer.Comment(0,0,result)

def AddNewLineNode(count:int = 1):
    return tcss.tokenizer.WhitespaceToken(0,0,"\n" * count)

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    
    CSSNodes = []
    CSSFiles = ["css/root.css",
                "css/ads.css",
                "css/diff.css",
                "css/headings.css",
                "css/images.css",
                "css/keyframes.css",
                "css/links.css",
                "css/localization.css",
                "css/main-page.css",
                "css/media.css",
                "css/mw-echo.css",
                "css/navigation.css",
                "css/oo-ui.css",
                "css/portable-infobox.css",
                "css/source-editor.css",
                "css/tabber.css",
                "css/tables.css",
                "css/toc.css",
                "css/video.css",
                "css/visual-editor.css",
                "css/wiki-templates.css",
            ]

    for filepath in CSSFiles:
        with open(filepath) as f:
            CSSNodes+= tcss.parse_stylesheet(f.read())
            CSSNodes.append(AddNewLineNode())
            CSSNodes.append(AddNewLineNode())

    with open('merged.css','w+') as f:
        for line in tcss.serialize(CSSNodes).split('\n'):
            f.write(line.replace("/palworld.wiki.gg/","") + '\n')
    