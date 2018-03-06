# -*- coding: utf-8 -*-

import sys
import re
import io

TXT_START='<P ParaShape="0" Style="0"><TEXT CharShape="0"><CHAR>'
TXT_END='</CHAR></TEXT></P>'

L1_START='<P ParaShape="1" Style="0"><TEXT CharShape="0"><CHAR>* '
L2_START='<P ParaShape="2" Style="0"><TEXT CharShape="0"><CHAR>  - '
L3_START='<P ParaShape="3" Style="0"><TEXT CharShape="0"><CHAR>    + '
L4_START='<P ParaShape="4" Style="0"><TEXT CharShape="0"><CHAR>      * '
L5_START='<P ParaShape="5" Style="0"><TEXT CharShape="0"><CHAR>        - '
L6_START='<P ParaShape="6" Style="0"><TEXT CharShape="0"><CHAR>          + '
H1_START='<P ParaShape="0" Style="0"><TEXT CharShape="1"><CHAR>'
H2_START='<P ParaShape="0" Style="0"><TEXT CharShape="2"><CHAR>'
H3_START='<P ParaShape="0" Style="0"><TEXT CharShape="3"><CHAR>'
H4_START='<P ParaShape="0" Style="0"><TEXT CharShape="4"><CHAR>'

HEADER="""<?xml version="1.0" encoding="UTF-8" standalone="no"?><HWPML Style="embed" SubVersion="9.0.1.0" Version="2.9"><HEAD SecCnt="1">
<DOCSUMMARY><TITLE>___TITLE___</TITLE><AUTHOR>___AUTHOR___</AUTHOR><DATE>___DATE___</DATE></DOCSUMMARY><DOCSETTING>
<BEGINNUMBER Endnote="1" Equation="1" Footnote="1" Page="1" Picture="1" Table="1" /><CARETPOS List="0" Para="20" Pos="6" /></DOCSETTING><MAPPINGTABLE><FACENAMELIST><FONTFACE Count="2" Lang="Hangul"><FONT Id="0" Name="함초롬돋움" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT><FONT Id="1" Name="함초롬바탕" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT></FONTFACE><FONTFACE Count="2" Lang="Latin"><FONT Id="0" Name="함초롬돋움" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT><FONT Id="1" Name="함초롬바탕" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT></FONTFACE><FONTFACE Count="2" Lang="Hanja"><FONT Id="0" Name="함초롬돋움" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT><FONT Id="1" Name="함초롬바탕" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT></FONTFACE><FONTFACE Count="2" Lang="Japanese"><FONT Id="0" Name="함초롬돋움" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT><FONT Id="1" Name="함초롬바탕" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT></FONTFACE><FONTFACE Count="2" Lang="Other"><FONT Id="0" Name="함초롬돋움" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT><FONT Id="1" Name="함초롬바탕" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT></FONTFACE><FONTFACE Count="2" Lang="Symbol"><FONT Id="0" Name="함초롬돋움" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT><FONT Id="1" Name="함초롬바탕" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT></FONTFACE><FONTFACE Count="2" Lang="User"><FONT Id="0" Name="함초롬돋움" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT><FONT Id="1" Name="함초롬바탕" Type="ttf"><TYPEINFO ArmStyle="1" Contrast="0" FamilyType="2" Letterform="1" Midline="1" Proportion="4" StrokeVariation="1" Weight="6" XHeight="1" /></FONT></FONTFACE></FACENAMELIST>
<CHARSHAPELIST Count="5">
    <CHARSHAPE BorderFillId="2" Height="1000" Id="0" ShadeColor="4294967295" SymMark="0" TextColor="0" UseFontSpace="false" UseKerning="false">
        <FONTID Hangul="1" Hanja="1" Japanese="1" Latin="1" Other="1" Symbol="1" User="1" />
        <RATIO Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
        <CHARSPACING Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        <RELSIZE Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
        <CHAROFFSET Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
    </CHARSHAPE>
    <CHARSHAPE BorderFillId="2" Height="2000" Id="1" ShadeColor="4294967295" SymMark="0" TextColor="0" UseFontSpace="false" UseKerning="false">
        <FONTID Hangul="1" Hanja="1" Japanese="1" Latin="1" Other="1" Symbol="1" User="1" />
        <RATIO Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
        <CHARSPACING Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        <RELSIZE Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
        <CHAROFFSET Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        <BOLD />
    </CHARSHAPE>
    <CHARSHAPE BorderFillId="2" Height="1600" Id="2" ShadeColor="4294967295" SymMark="0" TextColor="0" UseFontSpace="false" UseKerning="false">
        <FONTID Hangul="1" Hanja="1" Japanese="1" Latin="1" Other="1" Symbol="1" User="1" />
        <RATIO Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
        <CHARSPACING Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        <RELSIZE Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
        <CHAROFFSET Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        <BOLD />
    </CHARSHAPE>
    <CHARSHAPE BorderFillId="2" Height="1200" Id="3" ShadeColor="4294967295" SymMark="0" TextColor="0" UseFontSpace="false" UseKerning="false">
        <FONTID Hangul="1" Hanja="1" Japanese="1" Latin="1" Other="1" Symbol="1" User="1" />
        <RATIO Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
        <CHARSPACING Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        <RELSIZE Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
        <CHAROFFSET Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        <BOLD />
    </CHARSHAPE>
    <CHARSHAPE BorderFillId="2" Height="1000" Id="4" ShadeColor="4294967295" SymMark="0" TextColor="0" UseFontSpace="false" UseKerning="false">
        <FONTID Hangul="1" Hanja="1" Japanese="1" Latin="1" Other="1" Symbol="1" User="1" />
        <RATIO Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
        <CHARSPACING Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        <RELSIZE Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
        <CHAROFFSET Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        <BOLD />
    </CHARSHAPE>
    <CHARSHAPE BorderFillId="2" Height="2500" Id="5" ShadeColor="4294967295" SymMark="0" TextColor="0" UseFontSpace="false" UseKerning="false">
        <FONTID Hangul="1" Hanja="1" Japanese="1" Latin="1" Other="1" Symbol="1" User="1" />
        <RATIO Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
        <CHARSPACING Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        <RELSIZE Hangul="100" Hanja="100" Japanese="100" Latin="100" Other="100" Symbol="100" User="100" />
        <CHAROFFSET Hangul="0" Hanja="0" Japanese="0" Latin="0" Other="0" Symbol="0" User="0" />
        <BOLD />
    </CHARSHAPE>
</CHARSHAPELIST>
<PARASHAPELIST Count="9">
    <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="0" FontLineHeight="false" HeadingType="None" Id="0" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
        <PARAMARGIN Indent="0" Left="0" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
        <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" />
    </PARASHAPE>
    <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="0" FontLineHeight="false" HeadingType="None" Id="1" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
        <PARAMARGIN Indent="-2104" Left="0" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
        <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" />
    </PARASHAPE>
    <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="0" FontLineHeight="false" HeadingType="None" Id="2" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
        <PARAMARGIN Indent="-4174" Left="0" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
        <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" />
    </PARASHAPE>
    <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="0" FontLineHeight="false" HeadingType="None" Id="3" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
        <PARAMARGIN Indent="-6244" Left="0" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
        <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" />
    </PARASHAPE>
    <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="0" FontLineHeight="false" HeadingType="None" Id="4" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
        <PARAMARGIN Indent="-8314" Left="0" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
        <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" />
    </PARASHAPE>
    <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="0" FontLineHeight="false" HeadingType="None" Id="5" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
        <PARAMARGIN Indent="-10384" Left="0" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
        <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" />
    </PARASHAPE>
    <PARASHAPE Align="Justify" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="true" Condense="0" FontLineHeight="false" HeadingType="None" Id="6" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
        <PARAMARGIN Indent="-12454" Left="0" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
        <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" />
    </PARASHAPE>
    <PARASHAPE Align="Center" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="false" Condense="0" FontLineHeight="false" HeadingType="None" Id="7" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
        <PARAMARGIN Indent="0" Left="0" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
        <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" />
    </PARASHAPE>
    <PARASHAPE Align="Right" AutoSpaceEAsianEng="false" AutoSpaceEAsianNum="false" BreakLatinWord="KeepWord" BreakNonLatinWord="false" Condense="0" FontLineHeight="false" HeadingType="None" Id="8" KeepLines="false" KeepWithNext="false" Level="0" LineWrap="Break" PageBreakBefore="false" SnapToGrid="true" TabDef="0" VerAlign="Baseline" WidowOrphan="false">
        <PARAMARGIN Indent="0" Left="0" LineSpacing="160" LineSpacingType="Percent" Next="0" Prev="0" Right="0" />
        <PARABORDER BorderFill="2" Connect="false" IgnoreMargin="false" />
    </PARASHAPE>
</PARASHAPELIST>
</MAPPINGTABLE><COMPATIBLEDOCUMENT TargetProgram="None"><LAYOUTCOMPATIBILITY AdjustBaselineInFixedLinespacing="false" AdjustBaselineOfObjectToBottom="false" AdjustLineheightToFont="false" AdjustMarginFromAdjustLineheight="false" AdjustParaBorderOffsetWithBorder="false" AdjustParaBorderfillToSpacing="false" AdjustVertPosOfLine="false" ApplyAtLeastToPercent100Pct="false" ApplyCharSpacingToCharGrid="false" ApplyExtendHeaderFooterEachSection="false" ApplyFontWeightToBold="false" ApplyFontspaceToLatin="false" ApplyMinColumnWidthTo1mm="false" ApplyNextspacingOfLastPara="false" ApplyParaBorderToOutside="false" ApplyPrevspacingBeneathObject="false" ApplyTabPosBasedOnSegment="false" BaseCharUnitOfIndentOnFirstChar="false" BaseCharUnitOnEAsian="false" BaseLinespacingOnLinegrid="false" BreakTabOverLine="false" ConnectParaBorderfillOfEqualBorder="false" DoNotAdjustEmptyAnchorLine="false" DoNotAdjustWordInJustify="false" DoNotAlignLastForbidden="false" DoNotAlignLastPeriod="false" DoNotAlignWhitespaceOnRight="false" DoNotApplyAutoSpaceEAsianEng="false" DoNotApplyAutoSpaceEAsianNum="false" DoNotApplyColSeparatorAtNoGap="false" DoNotApplyExtensionCharCompose="false" DoNotApplyGridInHeaderFooter="false" DoNotApplyHeaderFooterAtNoSpace="false" DoNotApplyImageEffect="false" DoNotApplyLinegridAtNoLinespacing="false" DoNotApplyShapeComment="false" DoNotApplyStrikeoutWithUnderline="false" DoNotApplyVertOffsetOfForward="false" DoNotApplyWhiteSpaceHeight="false" DoNotFormattingAtBeneathAnchor="false" DoNotHoldAnchorOfTable="false" ExtendLineheightToOffset="false" ExtendLineheightToParaBorderOffset="false" ExtendVertLimitToPageMargins="false" FixedUnderlineWidth="false" OverlapBothAllowOverlap="false" TreatQuotationAsLatin="false" UseInnerUnderline="false" UseLowercaseStrikeout="false" /></COMPATIBLEDOCUMENT></HEAD><BODY><SECDEF CharGrid="0" FirstBorder="false" FirstFill="false" LineGrid="0" OutlineShape="1" SpaceColumns="1134" TabStop="8000" TextDirection="0" TextVerticalWidthHead="0"><STARTNUMBER Equation="0" Figure="0" Page="0" PageStartsOn="Both" Table="0" /><HIDE Border="false" EmptyLine="false" Fill="false" Footer="false" Header="false" MasterPage="false" PageNumPos="false" /><PAGEDEF GutterType="LeftOnly" Height="84188" Landscape="0" Width="59528"><PAGEMARGIN Bottom="4252" Footer="4252" Gutter="0" Header="4252" Left="8504" Right="8504" Top="5668" /></PAGEDEF><FOOTNOTESHAPE><AUTONUMFORMAT SuffixChar=")" Superscript="false" Type="Digit" /><NOTELINE Length="5cm" Type="Solid" Width="0.12mm" /><NOTESPACING AboveLine="850" BelowLine="567" BetweenNotes="283" /><NOTENUMBERING NewNumber="1" Type="Continuous" /><NOTEPLACEMENT BeneathText="false" Place="EachColumn" /></FOOTNOTESHAPE><ENDNOTESHAPE><AUTONUMFORMAT SuffixChar=")" Superscript="false" Type="Digit" /><NOTELINE Length="14692344" Type="Solid" Width="0.12mm" /><NOTESPACING AboveLine="850" BelowLine="567" BetweenNotes="0" /><NOTENUMBERING NewNumber="1" Type="Continuous" /><NOTEPLACEMENT BeneathText="false" Place="EndOfDocument" /></ENDNOTESHAPE><PAGEBORDERFILL BorferFill="1" FillArea="Paper" FooterInside="false" HeaderInside="false" TextBorder="true" Type="Both"><PAGEOFFSET Bottom="1417" Left="1417" Right="1417" Top="1417" /></PAGEBORDERFILL><PAGEBORDERFILL BorferFill="1" FillArea="Paper" FooterInside="false" HeaderInside="false" TextBorder="true" Type="Even"><PAGEOFFSET Bottom="1417" Left="1417" Right="1417" Top="1417" /></PAGEBORDERFILL><PAGEBORDERFILL BorferFill="1" FillArea="Paper" FooterInside="false" HeaderInside="false" TextBorder="true" Type="Odd"><PAGEOFFSET Bottom="1417" Left="1417" Right="1417" Top="1417" /></PAGEBORDERFILL></SECDEF><SECTION Id="0">"""

FOOTER="""</SECTION></BODY><TAIL></TAIL></HWPML>"""


INTRO="""
<P ParaShape="7" Style="0"><TEXT CharShape="5"><CHAR>___TITLE___</CHAR></TEXT></P>
<P ParaShape="8" Style="0"><TEXT CharShape="0"><CHAR>작성자 : ___AUTHOR___</CHAR></TEXT></P>
<P ParaShape="8" Style="0"><TEXT CharShape="0"><CHAR>작성일 : ___DATE___</CHAR></TEXT></P>
"""

fIn  = "README.md"
fOut = "readme.hml"

if len(sys.argv) > 1:
    fIn = sys.argv[1]

if len(sys.argv) > 2:
    fOut = sys.argv[2]

print("in:%s -> out:%s"%(fIn, fOut))


with open(fIn, 'r') as content_file:
    ret = content_file.read()

ret = re.sub("\r", "", ret)
t = re.search("(?<=title: ).*", ret).group(0)
a = re.search("(?<=author: ).*", ret).group(0)
d = re.search("(?<=date: ).*", ret).group(0)
ret = re.sub("---(.|\n)*---", "", ret)

ret = re.sub("\n[-+*] "                    , "\n"+L1_START, ret)
ret = re.sub("\n    [-+*] "                , "\n"+L2_START, ret)
ret = re.sub("\n        [-+*] "            , "\n"+L3_START, ret)
ret = re.sub("\n            [-+*] "        , "\n"+L4_START, ret)
ret = re.sub("\n                [-+*] "    , "\n"+L5_START, ret)
ret = re.sub("\n                    [-+*] ", "\n"+L6_START, ret)

ret = re.sub("\n# "     , "\n"+H1_START, ret)
ret = re.sub("\n## "    , "\n"+H2_START, ret)
ret = re.sub("\n### "   , "\n"+H3_START, ret)
ret = re.sub("\n#### "  , "\n"+H4_START, ret)
ret = re.sub("\n##### " , "\n"+H4_START, ret)
ret = re.sub("\n###### ", "\n"+H4_START, ret)

ret = re.sub("\n(?=[^<])", "\n"+TXT_START, ret)

ret = re.sub("\n", TXT_END+"\n", ret)
ret = re.sub("^"+TXT_END, "", ret)

ret = HEADER + INTRO + ret + FOOTER

ret = re.sub("___TITLE___" , t, ret)
ret = re.sub("___AUTHOR___", a, ret)
ret = re.sub("___DATE___"  , d, ret)

with io.open(fOut, "w", encoding="utf-8") as f:
    f.write(ret)
    f.close()
