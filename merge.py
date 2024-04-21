from glob import glob
import tinycss2 as tcss
import os

def RemoveComments(nodes: list):
    index = 0
    for node in nodes:
        if node.type == 'comment':
            nodes.pop(index)

        if hasattr(node,"content") and node.content:
            node.content = RemoveComments(node.content)
            
        if hasattr(node,"prelude") and node.prelude:
            node.prelude = RemoveComments(node.prelude)
            
        index += 1
        
    return nodes
    
def CreateCommentNode(*comment:str):
    result = "\n\t".join(comment)
    result = f"{"="*96}\n\t{result}\n{"="*96}"
    return tcss.tokenizer.Comment(0,0,result)

def CreateNewLineNode(count:int = 1):
    return tcss.tokenizer.WhitespaceToken(0,0,"\n" * count)

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    
    CSSNodes = []
    
    # This array determines concatenation order
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
                "css/light.css",
            ]

    for filepath in CSSFiles:
        with open(filepath) as f:
            CSSNodes+= tcss.parse_stylesheet(f.read())
            CSSNodes.append(CreateNewLineNode())
            CSSNodes.append(CreateNewLineNode())

    CSSNodes = RemoveComments(CSSNodes)
    
    CSSNodes.insert(0,CreateCommentNode("This is a merged stylesheet. For editing see https://github.com/kai13xd/PalworldWikiCSS"))
    CSSNodes.insert(1,CreateNewLineNode())
    with open('merged.css','w+') as f:
        for line in tcss.serialize(CSSNodes).split('\n'):
            f.write(line.replace("https://palworld.wiki.gg/","/") + '\n')
    