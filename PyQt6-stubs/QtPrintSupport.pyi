# The PEP 484 type hints stub file for the QtPrintSupport module.
#
# Generated by SIP 6.5.0
#
# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
#
# This file is part of PyQt6.
#
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
#
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

# Support for QDate, QDateTime and QTime.
import datetime
import enum
import typing

import PyQt6.sip
from PyQt6 import QtCore, QtGui, QtWidgets

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

class QAbstractPrintDialog(QtWidgets.QDialog):
    class PrintDialogOption(enum.Flag):
        PrintToFile = ...  # type: QAbstractPrintDialog.PrintDialogOption
        PrintSelection = ...  # type: QAbstractPrintDialog.PrintDialogOption
        PrintPageRange = ...  # type: QAbstractPrintDialog.PrintDialogOption
        PrintCollateCopies = ...  # type: QAbstractPrintDialog.PrintDialogOption
        PrintShowPageSize = ...  # type: QAbstractPrintDialog.PrintDialogOption
        PrintCurrentPage = ...  # type: QAbstractPrintDialog.PrintDialogOption
    class PrintRange(enum.Enum):
        AllPages = ...  # type: QAbstractPrintDialog.PrintRange
        Selection = ...  # type: QAbstractPrintDialog.PrintRange
        PageRange = ...  # type: QAbstractPrintDialog.PrintRange
        CurrentPage = ...  # type: QAbstractPrintDialog.PrintRange
    def __init__(self, printer: "QPrinter", parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    def setOptionTabs(self, tabs: typing.Iterable[QtWidgets.QWidget]) -> None: ...
    def printer(self) -> "QPrinter": ...
    def toPage(self) -> int: ...
    def fromPage(self) -> int: ...
    def setFromTo(self, fromPage: int, toPage: int) -> None: ...
    def maxPage(self) -> int: ...
    def minPage(self) -> int: ...
    def setMinMax(self, min: int, max: int) -> None: ...
    def printRange(self) -> "QAbstractPrintDialog.PrintRange": ...
    def setPrintRange(self, range: "QAbstractPrintDialog.PrintRange") -> None: ...

class QPageSetupDialog(QtWidgets.QDialog):
    @typing.overload
    def __init__(self, printer: "QPrinter", parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    @typing.overload
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    def printer(self) -> "QPrinter": ...
    def done(self, result: int) -> None: ...
    @typing.overload
    def open(self) -> None: ...
    @typing.overload
    def open(self, slot: PYQT_SLOT) -> None: ...
    def exec(self) -> int: ...
    def setVisible(self, visible: bool) -> None: ...

class QPrintDialog(QAbstractPrintDialog):
    @typing.overload
    def __init__(self, printer: "QPrinter", parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    @typing.overload
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    accepted: typing.ClassVar[QtCore.pyqtSignal]
    @typing.overload
    def open(self) -> None: ...
    @typing.overload
    def open(self, slot: PYQT_SLOT) -> None: ...
    def setVisible(self, visible: bool) -> None: ...
    def options(self) -> QAbstractPrintDialog.PrintDialogOption: ...
    def setOptions(self, options: QAbstractPrintDialog.PrintDialogOption) -> None: ...
    def testOption(self, option: QAbstractPrintDialog.PrintDialogOption) -> bool: ...
    def setOption(self, option: QAbstractPrintDialog.PrintDialogOption, on: bool = ...) -> None: ...
    def done(self, result: int) -> None: ...
    def exec(self) -> int: ...

class QPrintEngine(PyQt6.sip.simplewrapper):
    class PrintEnginePropertyKey(enum.Enum):
        PPK_CollateCopies = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_ColorMode = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_Creator = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_DocumentName = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_FullPage = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_NumberOfCopies = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_Orientation = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_OutputFileName = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PageOrder = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PageRect = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PageSize = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PaperRect = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PaperSource = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PrinterName = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PrinterProgram = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_Resolution = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_SelectionOption = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_SupportedResolutions = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_WindowsPageSize = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_FontEmbedding = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_Duplex = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PaperSources = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_CustomPaperSize = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PageMargins = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PaperSize = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_CopyCount = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_SupportsMultipleCopies = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PaperName = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_QPageSize = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_QPageMargins = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_QPageLayout = ...  # type: QPrintEngine.PrintEnginePropertyKey
        PPK_CustomBase = ...  # type: QPrintEngine.PrintEnginePropertyKey
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: "QPrintEngine") -> None: ...
    def printerState(self) -> "QPrinter.PrinterState": ...
    def metric(self, a0: QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def abort(self) -> bool: ...
    def newPage(self) -> bool: ...
    def property(self, key: "QPrintEngine.PrintEnginePropertyKey") -> typing.Any: ...
    def setProperty(self, key: "QPrintEngine.PrintEnginePropertyKey", value: typing.Any) -> None: ...

class QPrinter(QtGui.QPagedPaintDevice):
    class DuplexMode(enum.Enum):
        DuplexNone = ...  # type: QPrinter.DuplexMode
        DuplexAuto = ...  # type: QPrinter.DuplexMode
        DuplexLongSide = ...  # type: QPrinter.DuplexMode
        DuplexShortSide = ...  # type: QPrinter.DuplexMode
    class Unit(enum.Enum):
        Millimeter = ...  # type: QPrinter.Unit
        Point = ...  # type: QPrinter.Unit
        Inch = ...  # type: QPrinter.Unit
        Pica = ...  # type: QPrinter.Unit
        Didot = ...  # type: QPrinter.Unit
        Cicero = ...  # type: QPrinter.Unit
        DevicePixel = ...  # type: QPrinter.Unit
    class PrintRange(enum.Enum):
        AllPages = ...  # type: QPrinter.PrintRange
        Selection = ...  # type: QPrinter.PrintRange
        PageRange = ...  # type: QPrinter.PrintRange
        CurrentPage = ...  # type: QPrinter.PrintRange
    class OutputFormat(enum.Enum):
        NativeFormat = ...  # type: QPrinter.OutputFormat
        PdfFormat = ...  # type: QPrinter.OutputFormat
    class PrinterState(enum.Enum):
        Idle = ...  # type: QPrinter.PrinterState
        Active = ...  # type: QPrinter.PrinterState
        Aborted = ...  # type: QPrinter.PrinterState
        Error = ...  # type: QPrinter.PrinterState
    class PaperSource(enum.Enum):
        OnlyOne = ...  # type: QPrinter.PaperSource
        Lower = ...  # type: QPrinter.PaperSource
        Middle = ...  # type: QPrinter.PaperSource
        Manual = ...  # type: QPrinter.PaperSource
        Envelope = ...  # type: QPrinter.PaperSource
        EnvelopeManual = ...  # type: QPrinter.PaperSource
        Auto = ...  # type: QPrinter.PaperSource
        Tractor = ...  # type: QPrinter.PaperSource
        SmallFormat = ...  # type: QPrinter.PaperSource
        LargeFormat = ...  # type: QPrinter.PaperSource
        LargeCapacity = ...  # type: QPrinter.PaperSource
        Cassette = ...  # type: QPrinter.PaperSource
        FormSource = ...  # type: QPrinter.PaperSource
        MaxPageSource = ...  # type: QPrinter.PaperSource
        Upper = ...  # type: QPrinter.PaperSource
        CustomSource = ...  # type: QPrinter.PaperSource
        LastPaperSource = ...  # type: QPrinter.PaperSource
    class ColorMode(enum.Enum):
        GrayScale = ...  # type: QPrinter.ColorMode
        Color = ...  # type: QPrinter.ColorMode
    class PageOrder(enum.Enum):
        FirstPageFirst = ...  # type: QPrinter.PageOrder
        LastPageFirst = ...  # type: QPrinter.PageOrder
    class PrinterMode(enum.Enum):
        ScreenResolution = ...  # type: QPrinter.PrinterMode
        PrinterResolution = ...  # type: QPrinter.PrinterMode
        HighResolution = ...  # type: QPrinter.PrinterMode
    @typing.overload
    def __init__(self, mode: "QPrinter.PrinterMode" = ...) -> None: ...
    @typing.overload
    def __init__(self, printer: "QPrinterInfo", mode: "QPrinter.PrinterMode" = ...) -> None: ...
    def pdfVersion(self) -> QtGui.QPagedPaintDevice.PdfVersion: ...
    def setPdfVersion(self, version: QtGui.QPagedPaintDevice.PdfVersion) -> None: ...
    def setEngines(self, printEngine: QPrintEngine, paintEngine: QtGui.QPaintEngine) -> None: ...
    def metric(self, a0: QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def printRange(self) -> "QPrinter.PrintRange": ...
    def setPrintRange(self, range: "QPrinter.PrintRange") -> None: ...
    def toPage(self) -> int: ...
    def fromPage(self) -> int: ...
    def setFromTo(self, fromPage: int, toPage: int) -> None: ...
    def printEngine(self) -> QPrintEngine: ...
    def paintEngine(self) -> QtGui.QPaintEngine: ...
    def printerState(self) -> "QPrinter.PrinterState": ...
    def abort(self) -> bool: ...
    def newPage(self) -> bool: ...
    def pageRect(self, a0: "QPrinter.Unit") -> QtCore.QRectF: ...
    def paperRect(self, a0: "QPrinter.Unit") -> QtCore.QRectF: ...
    def fontEmbeddingEnabled(self) -> bool: ...
    def setFontEmbeddingEnabled(self, enable: bool) -> None: ...
    def supportedResolutions(self) -> typing.List[int]: ...
    def duplex(self) -> "QPrinter.DuplexMode": ...
    def setDuplex(self, duplex: "QPrinter.DuplexMode") -> None: ...
    def paperSource(self) -> "QPrinter.PaperSource": ...
    def setPaperSource(self, a0: "QPrinter.PaperSource") -> None: ...
    def supportsMultipleCopies(self) -> bool: ...
    def copyCount(self) -> int: ...
    def setCopyCount(self, a0: int) -> None: ...
    def fullPage(self) -> bool: ...
    def setFullPage(self, a0: bool) -> None: ...
    def collateCopies(self) -> bool: ...
    def setCollateCopies(self, collate: bool) -> None: ...
    def colorMode(self) -> "QPrinter.ColorMode": ...
    def setColorMode(self, a0: "QPrinter.ColorMode") -> None: ...
    def resolution(self) -> int: ...
    def setResolution(self, a0: int) -> None: ...
    def pageOrder(self) -> "QPrinter.PageOrder": ...
    def setPageOrder(self, a0: "QPrinter.PageOrder") -> None: ...
    def creator(self) -> str: ...
    def setCreator(self, a0: str) -> None: ...
    def docName(self) -> str: ...
    def setDocName(self, a0: str) -> None: ...
    def printProgram(self) -> str: ...
    def setPrintProgram(self, a0: str) -> None: ...
    def outputFileName(self) -> str: ...
    def setOutputFileName(self, a0: str) -> None: ...
    def isValid(self) -> bool: ...
    def printerName(self) -> str: ...
    def setPrinterName(self, a0: str) -> None: ...
    def outputFormat(self) -> "QPrinter.OutputFormat": ...
    def setOutputFormat(self, format: "QPrinter.OutputFormat") -> None: ...

class QPrinterInfo(PyQt6.sip.simplewrapper):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, src: "QPrinterInfo") -> None: ...
    @typing.overload
    def __init__(self, printer: QPrinter) -> None: ...
    def supportedColorModes(self) -> typing.List[QPrinter.ColorMode]: ...
    def defaultColorMode(self) -> QPrinter.ColorMode: ...
    def supportedDuplexModes(self) -> typing.List[QPrinter.DuplexMode]: ...
    def defaultDuplexMode(self) -> QPrinter.DuplexMode: ...
    @staticmethod
    def defaultPrinterName() -> str: ...
    @staticmethod
    def availablePrinterNames() -> typing.List[str]: ...
    def supportedResolutions(self) -> typing.List[int]: ...
    def maximumPhysicalPageSize(self) -> QtGui.QPageSize: ...
    def minimumPhysicalPageSize(self) -> QtGui.QPageSize: ...
    def supportsCustomPageSizes(self) -> bool: ...
    def defaultPageSize(self) -> QtGui.QPageSize: ...
    def supportedPageSizes(self) -> typing.List[QtGui.QPageSize]: ...
    def state(self) -> QPrinter.PrinterState: ...
    def isRemote(self) -> bool: ...
    @staticmethod
    def printerInfo(printerName: str) -> "QPrinterInfo": ...
    def makeAndModel(self) -> str: ...
    def location(self) -> str: ...
    def description(self) -> str: ...
    @staticmethod
    def defaultPrinter() -> "QPrinterInfo": ...
    @staticmethod
    def availablePrinters() -> typing.List["QPrinterInfo"]: ...
    def isDefault(self) -> bool: ...
    def isNull(self) -> bool: ...
    def printerName(self) -> str: ...

class QPrintPreviewDialog(QtWidgets.QDialog):
    @typing.overload
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: QtCore.Qt.WindowType = ...) -> None: ...
    @typing.overload
    def __init__(self, printer: QPrinter, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: QtCore.Qt.WindowType = ...) -> None: ...
    paintRequested: typing.ClassVar[QtCore.pyqtSignal]
    def done(self, result: int) -> None: ...
    def printer(self) -> QPrinter: ...
    @typing.overload
    def open(self) -> None: ...
    @typing.overload
    def open(self, slot: PYQT_SLOT) -> None: ...
    def setVisible(self, visible: bool) -> None: ...

class QPrintPreviewWidget(QtWidgets.QWidget):
    class ZoomMode(enum.Enum):
        CustomZoom = ...  # type: QPrintPreviewWidget.ZoomMode
        FitToWidth = ...  # type: QPrintPreviewWidget.ZoomMode
        FitInView = ...  # type: QPrintPreviewWidget.ZoomMode
    class ViewMode(enum.Enum):
        SinglePageView = ...  # type: QPrintPreviewWidget.ViewMode
        FacingPagesView = ...  # type: QPrintPreviewWidget.ViewMode
        AllPagesView = ...  # type: QPrintPreviewWidget.ViewMode
    @typing.overload
    def __init__(self, printer: QPrinter, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: QtCore.Qt.WindowType = ...) -> None: ...
    @typing.overload
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: QtCore.Qt.WindowType = ...) -> None: ...
    def pageCount(self) -> int: ...
    previewChanged: typing.ClassVar[QtCore.pyqtSignal]
    paintRequested: typing.ClassVar[QtCore.pyqtSignal]
    def updatePreview(self) -> None: ...
    def setAllPagesViewMode(self) -> None: ...
    def setFacingPagesViewMode(self) -> None: ...
    def setSinglePageViewMode(self) -> None: ...
    def setPortraitOrientation(self) -> None: ...
    def setLandscapeOrientation(self) -> None: ...
    def fitInView(self) -> None: ...
    def fitToWidth(self) -> None: ...
    def setCurrentPage(self, pageNumber: int) -> None: ...
    def setZoomMode(self, zoomMode: "QPrintPreviewWidget.ZoomMode") -> None: ...
    def setViewMode(self, viewMode: "QPrintPreviewWidget.ViewMode") -> None: ...
    def setOrientation(self, orientation: QtGui.QPageLayout.Orientation) -> None: ...
    def setZoomFactor(self, zoomFactor: float) -> None: ...
    def zoomOut(self, factor: float = ...) -> None: ...
    def zoomIn(self, factor: float = ...) -> None: ...
    def print(self) -> None: ...
    def setVisible(self, visible: bool) -> None: ...
    def currentPage(self) -> int: ...
    def zoomMode(self) -> "QPrintPreviewWidget.ZoomMode": ...
    def viewMode(self) -> "QPrintPreviewWidget.ViewMode": ...
    def orientation(self) -> QtGui.QPageLayout.Orientation: ...
    def zoomFactor(self) -> float: ...
