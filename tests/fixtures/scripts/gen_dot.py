"""
////
// This is a dot-file that contains the spec for a labeled digraph.
// See also the docs here: https://graphviz.org/doc/info/lang.html
////
digraph project_dependencies {
    // Graph & cluster attributes
    graph [
        margin = 1
        compound = true // allows edges between clusters
        fillcolor = white
        fontname = verdana
        fontsize = 10
        labeljust = l // aligns label to the left
        labelloc = t // puts label at top of diagram
        newrank = true
        nodesep = .25 // separation between nodes in inches (default is 0.25
        overlap = false // prism is also interesting
        rankdir = LR // LR (left-to-right) or TB (top-to-bottom)
        ranksep = 0.5 // separation between ranks in inches (default is 0.5)
        ratio = auto // aspect ratio. diagram is tighter when it is declared
        shape = box
        //splines = true // uses curved lines to avoid nodes
        style = "filled"
    ]

    // Node attributes
    node [
        fillcolor = blue
        fontname = verdana
        fontsize = 10
        margin = "0.1, 0.05"
        shape = box
        style = "filled, rounded"
    ]

    // Edge attributes
    edge [ arrowsize = 0.9; color=black; penwidth = 0.9 ]

    label = <
        <table border="0" cellborder="0" cellspacing="0">
            <tr><td align="left"><b>Project Dependencies, Artifacts, Deployments</b></td></tr>
            <tr><td align="left">Key: Yellow⇒3rd party libs; Green⇒Our libs; Red⇒External Services</td></tr>
            <tr><td></td></tr>
            <tr><td></td></tr>
            <tr><td></td></tr>
        </table>
    >

    // Main graph Node declarations
    libOne [fillcolor="#009E73" label="libOne.git"]; // green
    libTwo [fillcolor="#009E73" label="libTwo.git"]; // green
    pypi [fillcolor="#56B4E9", label="PyPI"]; // blue

    // Main graph linkages
    libTwo -> libOne [label="depends"];

    {libTwo,libOne} -> pypi [label="push"];
}
"""

import os


def main():
    folder = os.path.dirname(__file__)
    output = os.path.join(folder, "gen_dot.dot")
    with open(output, "w") as fhandle:
        fhandle.write(__doc__)


if __name__ == "__main__":
    main()
