---
title: Class PdfSaveOptions
second_title: Aspose.TeX for .NET API Reference
description: Aspose.TeX.Presentation.Pdf.PdfSaveOptions class. Class representing options of saving to PDF
type: docs
weight: 710
url: /net/aspose.tex.presentation.pdf/pdfsaveoptions/
---
## PdfSaveOptions class

Class representing options of saving to PDF.

```csharp
public class PdfSaveOptions : SaveOptions
```

## Constructors

| Name | Description |
| --- | --- |
| [PdfSaveOptions](pdfsaveoptions/)() | Creates new instance of options. |

## Properties

| Name | Description |
| --- | --- |
| [EncryptionDetails](../../aspose.tex.presentation.pdf/pdfsaveoptions/encryptiondetails/) { get; set; } | Gets or sets a encryption details. If not set, then no encryption will be performed. |
| [ImageCompression](../../aspose.tex.presentation.pdf/pdfsaveoptions/imagecompression/) { get; set; } | Specifies compression type to be used for all images in the document. Default is Auto. |
| [JpegQualityLevel](../../aspose.tex.presentation.pdf/pdfsaveoptions/jpegqualitylevel/) { get; set; } | The Quality category specifies the level of compression for an image. Available values are 0 to 100. The lower the number specified, the higher the compression and therefore the lower the quality of the image. 0 value results in lowest quality image, while 100 results in highest. |
| [OutlineTreeExpansionLevel](../../aspose.tex.presentation.pdf/pdfsaveoptions/outlinetreeexpansionlevel/) { get; set; } | Specifies up to what level the document outline should be expanded when the PDF file is viewed. 1 - only the first level outline items are shown, 2 - only the first and second level outline items are shown, and so on. Default is 1. |
| [OutlineTreeHeight](../../aspose.tex.presentation.pdf/pdfsaveoptions/outlinetreeheight/) { get; set; } | Specifies the height of the document outline tree to save. 0 - the outline tree will not be converted, 1 - only the first level outline items will be converted, ans so on. |
| [RasterizeFormulas](../../aspose.tex.presentation/saveoptions/rasterizeformulas/) { get; set; } | Gets/sets the flag that allows to rasterize math formulas. |
| [RasterizeIncludedGraphics](../../aspose.tex.presentation/saveoptions/rasterizeincludedgraphics/) { get; set; } | Gets/sets the flag that allows to rasterize PS/EPS and/or XPS/OXPS included graphics. |
| [SubsetFonts](../../aspose.tex.presentation/saveoptions/subsetfonts/) { get; set; } | Gets/sets the flag indicating whether to subset fonts in output file or not. |
| [TextCompression](../../aspose.tex.presentation.pdf/pdfsaveoptions/textcompression/) { get; set; } | Specifies compression type to be used for all content streams except images. Default is Flate. |

### See Also

* class [SaveOptions](../../aspose.tex.presentation/saveoptions/)
* namespace [Aspose.TeX.Presentation.Pdf](../../aspose.tex.presentation.pdf/)
* assembly [Aspose.TeX](../../)


