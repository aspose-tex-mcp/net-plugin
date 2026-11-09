---
title: Class TeXOptions
second_title: Aspose.TeX for .NET API Reference
description: Aspose.TeX.TeXOptions class. TeX file processing options class
type: docs
weight: 840
url: /net/aspose.tex/texoptions/
---
## TeXOptions class

TeX file processing options class.

```csharp
public class TeXOptions
```

## Properties

| Name | Description |
| --- | --- |
| [DateTime](../../aspose.tex/texoptions/datetime/) { get; set; } | Gets/sets a certain value for date/time primitives like \year, \month, \day and \time. |
| [Executables](../../aspose.tex/texoptions/executables/) { get; } | A customizable collection of objects that emulate executables, which can be executed using the \write18 commands in Object TeX. |
| [FullInputFileNames](../../aspose.tex/texoptions/fullinputfilenames/) { get; set; } | Gets/sets the flag indicating whether full or short filenames are output to the transcript file and to the terminal when file input begins. |
| [IgnoreMissingPackages](../../aspose.tex/texoptions/ignoremissingpackages/) { get; set; } | Gets/sets the flag that instructs the engine whether to halt on missing package read attempt or ignore it. |
| [InputWorkingDirectory](../../aspose.tex/texoptions/inputworkingdirectory/) { get; set; } | Gets/sets input working directory. |
| [Interaction](../../aspose.tex/texoptions/interaction/) { get; set; } | Gets/sets the interaction mode to run a TeX engine in. |
| [JobName](../../aspose.tex/texoptions/jobname/) { get; set; } | Gets/set the name of the job. |
| [NoLigatures](../../aspose.tex/texoptions/noligatures/) { get; set; } | Gets/sets the flag that cancels ligatures in all fonts. |
| [OutputWorkingDirectory](../../aspose.tex/texoptions/outputworkingdirectory/) { get; set; } | Gets/sets output working directory. |
| [Repeat](../../aspose.tex/texoptions/repeat/) { get; set; } | Gets/sets the flag that indicates whether it is necessary to run the TeX job twice in case, for example, there are references in input TeX file(s). In general, this behavior is useful when the engine collects some data along the typesetting process and stores it in an auxilliary file, all at the first run. And at the second run, the engine somehow uses that data. |
| [RequiredInputDirectory](../../aspose.tex/texoptions/requiredinputdirectory/) { get; set; } | Gets/sets the directory for the required input, e.g., packages that are beyond Aspose.TeX's LaTeX support. |
| [SaveOptions](../../aspose.tex/texoptions/saveoptions/) { get; set; } | Gets/sets options used for rendering into destination format (XPS, PDF, image, etc.). Default value is the set of default options for rendering to XPS. |
| [ShellMode](../../aspose.tex/texoptions/shellmode/) { get; set; } | Determines the availability of \write18. |
| [TerminalIn](../../aspose.tex/texoptions/terminalin/) { get; set; } | Gets/sets the input terminal reader. |
| [TerminalOut](../../aspose.tex/texoptions/terminalout/) { get; set; } | Gets/sets the output terminal writer. |

## Methods

| Name | Description |
| --- | --- |
| static [ConsoleAppOptions](../../aspose.tex/texoptions/consoleappoptions/)(TeXConfig) | Returns options for use in a console application. |

### See Also

* namespace [Aspose.TeX](../../aspose.tex/)
* assembly [Aspose.TeX](../../)


