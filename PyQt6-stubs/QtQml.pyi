# The PEP 484 type hints stub file for the QtQml module.
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
from PyQt6 import QtCore, QtNetwork

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

class QJSEngine(QtCore.QObject):
    class ObjectOwnership(enum.Enum):
        CppOwnership = ...  # type: QJSEngine.ObjectOwnership
        JavaScriptOwnership = ...  # type: QJSEngine.ObjectOwnership
    class Extension(enum.Flag):
        TranslationExtension = ...  # type: QJSEngine.Extension
        ConsoleExtension = ...  # type: QJSEngine.Extension
        GarbageCollectionExtension = ...  # type: QJSEngine.Extension
        AllExtensions = ...  # type: QJSEngine.Extension
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: QtCore.QObject) -> None: ...
    def newSymbol(self, name: str) -> "QJSValue": ...
    def registerModule(self, moduleName: str, value: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]) -> bool: ...
    uiLanguageChanged: typing.ClassVar[QtCore.pyqtSignal]
    def catchError(self) -> "QJSValue": ...
    def hasError(self) -> bool: ...
    @staticmethod
    def objectOwnership(a0: QtCore.QObject) -> "QJSEngine.ObjectOwnership": ...
    @staticmethod
    def setObjectOwnership(a0: QtCore.QObject, a1: "QJSEngine.ObjectOwnership") -> None: ...
    def setUiLanguage(self, language: str) -> None: ...
    def uiLanguage(self) -> str: ...
    def isInterrupted(self) -> bool: ...
    def setInterrupted(self, interrupted: bool) -> None: ...
    @typing.overload
    def throwError(self, message: str) -> None: ...
    @typing.overload
    def throwError(self, error: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]) -> None: ...
    @typing.overload
    def throwError(self, errorType: "QJSValue.ErrorType", message: str = ...) -> None: ...
    def newErrorObject(self, errorType: "QJSValue.ErrorType", message: str = ...) -> "QJSValue": ...
    def importModule(self, fileName: str) -> "QJSValue": ...
    def newQMetaObject(self, metaObject: QtCore.QMetaObject) -> "QJSValue": ...
    def installExtensions(self, extensions: "QJSEngine.Extension", object: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str] = ...) -> None: ...
    def collectGarbage(self) -> None: ...
    def newQObject(self, object: QtCore.QObject) -> "QJSValue": ...
    def newArray(self, length: int = ...) -> "QJSValue": ...
    def newObject(self) -> "QJSValue": ...
    def evaluate(self, program: str, fileName: str = ..., lineNumber: int = ..., exceptionStackTrace: typing.Optional[typing.List[str]] = ...) -> "QJSValue": ...
    def globalObject(self) -> "QJSValue": ...

class QJSManagedValue(PyQt6.sip.simplewrapper):
    class Type(enum.Enum):
        Undefined = ...  # type: QJSManagedValue.Type
        Boolean = ...  # type: QJSManagedValue.Type
        Number = ...  # type: QJSManagedValue.Type
        String = ...  # type: QJSManagedValue.Type
        Object = ...  # type: QJSManagedValue.Type
        Symbol = ...  # type: QJSManagedValue.Type
        Function = ...  # type: QJSManagedValue.Type
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, value: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str], engine: QJSEngine) -> None: ...
    @typing.overload
    def __init__(self, value: "QJSPrimitiveValue", engine: QJSEngine) -> None: ...
    @typing.overload
    def __init__(self, string: str, engine: QJSEngine) -> None: ...
    @typing.overload
    def __init__(self, variant: typing.Any, engine: QJSEngine) -> None: ...
    def callAsConstructor(self, arguments: typing.Iterable[typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]] = ...) -> "QJSValue": ...
    def callWithInstance(self, instance: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str], arguments: typing.Iterable[typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]] = ...) -> "QJSValue": ...
    def call(self, arguments: typing.Iterable[typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]] = ...) -> "QJSValue": ...
    @typing.overload
    def deleteProperty(self, name: str) -> bool: ...
    @typing.overload
    def deleteProperty(self, arrayIndex: int) -> bool: ...
    @typing.overload
    def setProperty(self, name: str, value: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]) -> None: ...
    @typing.overload
    def setProperty(self, arrayIndex: int, value: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]) -> None: ...
    @typing.overload
    def property(self, name: str) -> "QJSValue": ...
    @typing.overload
    def property(self, arrayIndex: int) -> "QJSValue": ...
    @typing.overload
    def hasOwnProperty(self, name: str) -> bool: ...
    @typing.overload
    def hasOwnProperty(self, arrayIndex: int) -> bool: ...
    @typing.overload
    def hasProperty(self, name: str) -> bool: ...
    @typing.overload
    def hasProperty(self, arrayIndex: int) -> bool: ...
    def toDateTime(self) -> QtCore.QDateTime: ...
    def toQMetaObject(self) -> QtCore.QMetaObject: ...
    def toQObject(self) -> QtCore.QObject: ...
    def toUrl(self) -> QtCore.QUrl: ...
    def toRegularExpression(self) -> QtCore.QRegularExpression: ...
    def toInteger(self) -> int: ...
    def toVariant(self) -> typing.Any: ...
    def toJSValue(self) -> "QJSValue": ...
    def toPrimitive(self) -> "QJSPrimitiveValue": ...
    def toBoolean(self) -> bool: ...
    def toNumber(self) -> float: ...
    def toString(self) -> str: ...
    def isError(self) -> bool: ...
    def isDate(self) -> bool: ...
    def isQMetaObject(self) -> bool: ...
    def isQObject(self) -> bool: ...
    def isVariant(self) -> bool: ...
    def isUrl(self) -> bool: ...
    def isArray(self) -> bool: ...
    def isRegularExpression(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isInteger(self) -> bool: ...
    def isFunction(self) -> bool: ...
    def isSymbol(self) -> bool: ...
    def isObject(self) -> bool: ...
    def isString(self) -> bool: ...
    def isNumber(self) -> bool: ...
    def isBoolean(self) -> bool: ...
    def isUndefined(self) -> bool: ...
    def type(self) -> "QJSManagedValue.Type": ...
    def setPrototype(self, prototype: "QJSManagedValue") -> None: ...
    def prototype(self) -> "QJSManagedValue": ...
    def engine(self) -> QJSEngine: ...
    def strictlyEquals(self, other: "QJSManagedValue") -> bool: ...
    def equals(self, other: "QJSManagedValue") -> bool: ...

class QJSPrimitiveUndefined(PyQt6.sip.simplewrapper):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: "QJSPrimitiveUndefined") -> None: ...

class QJSPrimitiveNull(PyQt6.sip.simplewrapper):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: "QJSPrimitiveNull") -> None: ...

class QJSPrimitiveValue(PyQt6.sip.simplewrapper):
    class Type(enum.Enum):
        Undefined = ...  # type: QJSPrimitiveValue.Type
        Null = ...  # type: QJSPrimitiveValue.Type
        Boolean = ...  # type: QJSPrimitiveValue.Type
        Integer = ...  # type: QJSPrimitiveValue.Type
        Double = ...  # type: QJSPrimitiveValue.Type
        String = ...  # type: QJSPrimitiveValue.Type
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, undefined: QJSPrimitiveUndefined) -> None: ...
    @typing.overload
    def __init__(self, null: QJSPrimitiveNull) -> None: ...
    @typing.overload
    def __init__(self, value: bool) -> None: ...
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: float) -> None: ...
    @typing.overload
    def __init__(self, string: str) -> None: ...
    @typing.overload
    def __init__(self, a0: "QJSPrimitiveValue") -> None: ...
    def __neg__(self) -> "QJSPrimitiveValue": ...
    def __pos__(self) -> "QJSPrimitiveValue": ...
    def equals(self, other: "QJSPrimitiveValue") -> bool: ...
    def strictlyEquals(self, other: "QJSPrimitiveValue") -> bool: ...
    def toString(self) -> str: ...
    def toDouble(self) -> float: ...
    def toInteger(self) -> int: ...
    def toBoolean(self) -> bool: ...
    def type(self) -> "QJSPrimitiveValue.Type": ...

class QJSValue(PyQt6.sip.simplewrapper):
    class ErrorType(enum.Enum):
        GenericError = ...  # type: QJSValue.ErrorType
        EvalError = ...  # type: QJSValue.ErrorType
        RangeError = ...  # type: QJSValue.ErrorType
        ReferenceError = ...  # type: QJSValue.ErrorType
        SyntaxError = ...  # type: QJSValue.ErrorType
        TypeError = ...  # type: QJSValue.ErrorType
        URIError = ...  # type: QJSValue.ErrorType
    class ObjectConversionBehavior(enum.Enum):
        ConvertJSObjects = ...  # type: QJSValue.ObjectConversionBehavior
        RetainJSObjects = ...  # type: QJSValue.ObjectConversionBehavior
    class SpecialValue(enum.Enum):
        NullValue = ...  # type: QJSValue.SpecialValue
        UndefinedValue = ...  # type: QJSValue.SpecialValue
    @typing.overload
    def __init__(self, value: "QJSValue.SpecialValue" = ...) -> None: ...
    @typing.overload
    def __init__(self, other: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]) -> None: ...
    def errorType(self) -> "QJSValue.ErrorType": ...
    def callAsConstructor(self, args: typing.Iterable[typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]] = ...) -> "QJSValue": ...
    def callWithInstance(self, instance: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str], args: typing.Iterable[typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]] = ...) -> "QJSValue": ...
    def call(self, args: typing.Iterable[typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]] = ...) -> "QJSValue": ...
    def isCallable(self) -> bool: ...
    def deleteProperty(self, name: str) -> bool: ...
    def hasOwnProperty(self, name: str) -> bool: ...
    def hasProperty(self, name: str) -> bool: ...
    @typing.overload
    def setProperty(self, name: str, value: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]) -> None: ...
    @typing.overload
    def setProperty(self, arrayIndex: int, value: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]) -> None: ...
    @typing.overload
    def property(self, name: str) -> "QJSValue": ...
    @typing.overload
    def property(self, arrayIndex: int) -> "QJSValue": ...
    def setPrototype(self, prototype: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]) -> None: ...
    def prototype(self) -> "QJSValue": ...
    def strictlyEquals(self, other: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]) -> bool: ...
    def equals(self, other: typing.Union["QJSValue", "QJSValue.SpecialValue", bool, int, float, str]) -> bool: ...
    def toDateTime(self) -> QtCore.QDateTime: ...
    def toQObject(self) -> QtCore.QObject: ...
    def toPrimitive(self) -> QJSPrimitiveValue: ...
    @typing.overload
    def toVariant(self) -> typing.Any: ...
    @typing.overload
    def toVariant(self, behavior: "QJSValue.ObjectConversionBehavior") -> typing.Any: ...
    def toBool(self) -> bool: ...
    def toUInt(self) -> int: ...
    def toInt(self) -> int: ...
    def toNumber(self) -> float: ...
    def toString(self) -> str: ...
    def isUrl(self) -> bool: ...
    def isError(self) -> bool: ...
    def isArray(self) -> bool: ...
    def isRegExp(self) -> bool: ...
    def isDate(self) -> bool: ...
    def isObject(self) -> bool: ...
    def isQObject(self) -> bool: ...
    def isVariant(self) -> bool: ...
    def isUndefined(self) -> bool: ...
    def isString(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isNumber(self) -> bool: ...
    def isBool(self) -> bool: ...

class QJSValueIterator(PyQt6.sip.simplewrapper):
    def __init__(self, value: typing.Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]) -> None: ...
    def value(self) -> QJSValue: ...
    def name(self) -> str: ...
    def next(self) -> bool: ...
    def hasNext(self) -> bool: ...

class QQmlAbstractUrlInterceptor(PyQt6.sip.simplewrapper):
    class DataType(enum.Enum):
        QmlFile = ...  # type: QQmlAbstractUrlInterceptor.DataType
        JavaScriptFile = ...  # type: QQmlAbstractUrlInterceptor.DataType
        QmldirFile = ...  # type: QQmlAbstractUrlInterceptor.DataType
        UrlString = ...  # type: QQmlAbstractUrlInterceptor.DataType
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: "QQmlAbstractUrlInterceptor") -> None: ...
    def intercept(self, path: QtCore.QUrl, type: "QQmlAbstractUrlInterceptor.DataType") -> QtCore.QUrl: ...

class QQmlEngine(QJSEngine):
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    def urlInterceptors(self) -> typing.List[QQmlAbstractUrlInterceptor]: ...
    def interceptUrl(self, url: QtCore.QUrl, type: QQmlAbstractUrlInterceptor.DataType) -> QtCore.QUrl: ...
    def removeUrlInterceptor(self, urlInterceptor: QQmlAbstractUrlInterceptor) -> None: ...
    def addUrlInterceptor(self, urlInterceptor: QQmlAbstractUrlInterceptor) -> None: ...
    def singletonInstance(self, qmlTypeId: int) -> QtCore.QObject: ...
    def offlineStorageDatabaseFilePath(self, databaseName: str) -> str: ...
    exit: typing.ClassVar[QtCore.pyqtSignal]
    warnings: typing.ClassVar[QtCore.pyqtSignal]
    quit: typing.ClassVar[QtCore.pyqtSignal]
    def event(self, a0: QtCore.QEvent) -> bool: ...
    def retranslate(self) -> None: ...
    @staticmethod
    def setContextForObject(a0: QtCore.QObject, a1: "QQmlContext") -> None: ...
    @staticmethod
    def contextForObject(a0: QtCore.QObject) -> "QQmlContext": ...
    def setOutputWarningsToStandardError(self, a0: bool) -> None: ...
    def outputWarningsToStandardError(self) -> bool: ...
    def setBaseUrl(self, a0: QtCore.QUrl) -> None: ...
    def baseUrl(self) -> QtCore.QUrl: ...
    def offlineStoragePath(self) -> str: ...
    def setOfflineStoragePath(self, dir: str) -> None: ...
    def incubationController(self) -> "QQmlIncubationController": ...
    def setIncubationController(self, a0: "QQmlIncubationController") -> None: ...
    def removeImageProvider(self, id: str) -> None: ...
    def imageProvider(self, id: str) -> "QQmlImageProviderBase": ...
    def addImageProvider(self, id: str, a1: "QQmlImageProviderBase") -> None: ...
    def networkAccessManager(self) -> QtNetwork.QNetworkAccessManager: ...
    def networkAccessManagerFactory(self) -> "QQmlNetworkAccessManagerFactory": ...
    def setNetworkAccessManagerFactory(self, a0: "QQmlNetworkAccessManagerFactory") -> None: ...
    def importPlugin(self, filePath: str, uri: str, errors: typing.Iterable["QQmlError"]) -> bool: ...
    def addPluginPath(self, dir: str) -> None: ...
    def setPluginPathList(self, paths: typing.Iterable[str]) -> None: ...
    def pluginPathList(self) -> typing.List[str]: ...
    def addImportPath(self, dir: str) -> None: ...
    def setImportPathList(self, paths: typing.Iterable[str]) -> None: ...
    def importPathList(self) -> typing.List[str]: ...
    def trimComponentCache(self) -> None: ...
    def clearComponentCache(self) -> None: ...
    def rootContext(self) -> "QQmlContext": ...

class QQmlApplicationEngine(QQmlEngine):
    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, url: QtCore.QUrl, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, filePath: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    objectCreated: typing.ClassVar[QtCore.pyqtSignal]
    def setInitialProperties(self, initialProperties: typing.Dict[str, typing.Any]) -> None: ...
    def setExtraFileSelectors(self, extraFileSelectors: typing.Iterable[str]) -> None: ...
    def loadData(self, data: QtCore.QByteArray, url: QtCore.QUrl = ...) -> None: ...
    @typing.overload
    def load(self, url: QtCore.QUrl) -> None: ...
    @typing.overload
    def load(self, filePath: str) -> None: ...
    def rootObjects(self) -> typing.List[QtCore.QObject]: ...

class QQmlComponent(QtCore.QObject):
    class Status(enum.Enum):
        Null = ...  # type: QQmlComponent.Status
        Ready = ...  # type: QQmlComponent.Status
        Loading = ...  # type: QQmlComponent.Status
        Error = ...  # type: QQmlComponent.Status
    class CompilationMode(enum.Enum):
        PreferSynchronous = ...  # type: QQmlComponent.CompilationMode
        Asynchronous = ...  # type: QQmlComponent.CompilationMode
    @typing.overload
    def __init__(self, a0: QQmlEngine, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, a0: QQmlEngine, fileName: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, a0: QQmlEngine, fileName: str, mode: "QQmlComponent.CompilationMode", parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, a0: QQmlEngine, url: QtCore.QUrl, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, a0: QQmlEngine, url: QtCore.QUrl, mode: "QQmlComponent.CompilationMode", parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    def setInitialProperties(self, component: QtCore.QObject, properties: typing.Dict[str, typing.Any]) -> None: ...
    def engine(self) -> QQmlEngine: ...
    progressChanged: typing.ClassVar[QtCore.pyqtSignal]
    statusChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setData(self, a0: QtCore.QByteArray, baseUrl: QtCore.QUrl) -> None: ...
    @typing.overload
    def loadUrl(self, url: QtCore.QUrl) -> None: ...
    @typing.overload
    def loadUrl(self, url: QtCore.QUrl, mode: "QQmlComponent.CompilationMode") -> None: ...
    def creationContext(self) -> "QQmlContext": ...
    def completeCreate(self) -> None: ...
    def beginCreate(self, a0: "QQmlContext") -> QtCore.QObject: ...
    def createWithInitialProperties(self, initialProperties: typing.Dict[str, typing.Any], context: typing.Optional["QQmlContext"] = ...) -> QtCore.QObject: ...
    @typing.overload
    def create(self, context: typing.Optional["QQmlContext"] = ...) -> QtCore.QObject: ...
    @typing.overload
    def create(self, a0: "QQmlIncubator", context: typing.Optional["QQmlContext"] = ..., forContext: typing.Optional["QQmlContext"] = ...) -> None: ...
    def url(self) -> QtCore.QUrl: ...
    def progress(self) -> float: ...
    def errors(self) -> typing.List["QQmlError"]: ...
    def isLoading(self) -> bool: ...
    def isError(self) -> bool: ...
    def isReady(self) -> bool: ...
    def isNull(self) -> bool: ...
    def status(self) -> "QQmlComponent.Status": ...

class QQmlContext(QtCore.QObject):
    class PropertyPair(PyQt6.sip.simplewrapper):

        name = ...  # type: str
        value = ...  # type: typing.Any
        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, a0: "QQmlContext.PropertyPair") -> None: ...
    @typing.overload
    def __init__(self, engine: QQmlEngine, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, parentContext: "QQmlContext", parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    def objectForName(self, a0: str) -> QtCore.QObject: ...
    def setContextProperties(self, properties: typing.Iterable["QQmlContext.PropertyPair"]) -> None: ...
    def baseUrl(self) -> QtCore.QUrl: ...
    def setBaseUrl(self, a0: QtCore.QUrl) -> None: ...
    def resolvedUrl(self, a0: QtCore.QUrl) -> QtCore.QUrl: ...
    def nameForObject(self, a0: QtCore.QObject) -> str: ...
    @typing.overload
    def setContextProperty(self, a0: str, a1: QtCore.QObject) -> None: ...
    @typing.overload
    def setContextProperty(self, a0: str, a1: typing.Any) -> None: ...
    def contextProperty(self, a0: str) -> typing.Any: ...
    def setContextObject(self, a0: QtCore.QObject) -> None: ...
    def contextObject(self) -> QtCore.QObject: ...
    def parentContext(self) -> "QQmlContext": ...
    def engine(self) -> QQmlEngine: ...
    def isValid(self) -> bool: ...

class QQmlImageProviderBase(QtCore.QObject):
    class Flag(enum.Flag):
        ForceAsynchronousImageLoading = ...  # type: QQmlImageProviderBase.Flag
    class ImageType(enum.Enum):
        Image = ...  # type: QQmlImageProviderBase.ImageType
        Pixmap = ...  # type: QQmlImageProviderBase.ImageType
        Texture = ...  # type: QQmlImageProviderBase.ImageType
        ImageResponse = ...  # type: QQmlImageProviderBase.ImageType
    def flags(self) -> "QQmlImageProviderBase.Flag": ...
    def imageType(self) -> "QQmlImageProviderBase.ImageType": ...

class QQmlError(PyQt6.sip.simplewrapper):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: "QQmlError") -> None: ...
    def setMessageType(self, messageType: QtCore.QtMsgType) -> None: ...
    def messageType(self) -> QtCore.QtMsgType: ...
    def setObject(self, a0: QtCore.QObject) -> None: ...
    def object(self) -> QtCore.QObject: ...
    def toString(self) -> str: ...
    def setColumn(self, a0: int) -> None: ...
    def column(self) -> int: ...
    def setLine(self, a0: int) -> None: ...
    def line(self) -> int: ...
    def setDescription(self, a0: str) -> None: ...
    def description(self) -> str: ...
    def setUrl(self, a0: QtCore.QUrl) -> None: ...
    def url(self) -> QtCore.QUrl: ...
    def isValid(self) -> bool: ...

class QQmlExpression(QtCore.QObject):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: QQmlContext, a1: QtCore.QObject, a2: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, a0: "QQmlScriptString", context: typing.Optional[QQmlContext] = ..., scope: typing.Optional[QtCore.QObject] = ..., parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    valueChanged: typing.ClassVar[QtCore.pyqtSignal]
    def evaluate(self) -> typing.Tuple[typing.Any, bool]: ...
    def error(self) -> QQmlError: ...
    def clearError(self) -> None: ...
    def hasError(self) -> bool: ...
    def scopeObject(self) -> QtCore.QObject: ...
    def setSourceLocation(self, fileName: str, line: int, column: int = ...) -> None: ...
    def columnNumber(self) -> int: ...
    def lineNumber(self) -> int: ...
    def sourceFile(self) -> str: ...
    def setNotifyOnValueChanged(self, a0: bool) -> None: ...
    def notifyOnValueChanged(self) -> bool: ...
    def setExpression(self, a0: str) -> None: ...
    def expression(self) -> str: ...
    def context(self) -> QQmlContext: ...
    def engine(self) -> QQmlEngine: ...

class QQmlExtensionPlugin(QtCore.QObject):
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    def unregisterTypes(self) -> None: ...
    def baseUrl(self) -> QtCore.QUrl: ...
    def registerTypes(self, uri: str) -> None: ...

class QQmlEngineExtensionPlugin(QtCore.QObject):
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    def initializeEngine(self, engine: QQmlEngine, uri: str) -> None: ...

class QQmlFileSelector(QtCore.QObject):
    def __init__(self, engine: QQmlEngine, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    def selector(self) -> QtCore.QFileSelector: ...
    def setExtraSelectors(self, strings: typing.Iterable[str]) -> None: ...
    def setSelector(self, selector: QtCore.QFileSelector) -> None: ...

class QQmlIncubator(PyQt6.sip.simplewrapper):
    class Status(enum.Enum):
        Null = ...  # type: QQmlIncubator.Status
        Ready = ...  # type: QQmlIncubator.Status
        Loading = ...  # type: QQmlIncubator.Status
        Error = ...  # type: QQmlIncubator.Status
    class IncubationMode(enum.Enum):
        Asynchronous = ...  # type: QQmlIncubator.IncubationMode
        AsynchronousIfNested = ...  # type: QQmlIncubator.IncubationMode
        Synchronous = ...  # type: QQmlIncubator.IncubationMode
    def __init__(self, mode: "QQmlIncubator.IncubationMode" = ...) -> None: ...
    def setInitialState(self, a0: QtCore.QObject) -> None: ...
    def statusChanged(self, a0: "QQmlIncubator.Status") -> None: ...
    def setInitialProperties(self, initialProperties: typing.Dict[str, typing.Any]) -> None: ...
    def object(self) -> QtCore.QObject: ...
    def status(self) -> "QQmlIncubator.Status": ...
    def incubationMode(self) -> "QQmlIncubator.IncubationMode": ...
    def errors(self) -> typing.List[QQmlError]: ...
    def isLoading(self) -> bool: ...
    def isError(self) -> bool: ...
    def isReady(self) -> bool: ...
    def isNull(self) -> bool: ...
    def forceCompletion(self) -> None: ...
    def clear(self) -> None: ...

class QQmlIncubationController(PyQt6.sip.simplewrapper):
    def __init__(self) -> None: ...
    def incubatingObjectCountChanged(self, a0: int) -> None: ...
    def incubateFor(self, msecs: int) -> None: ...
    def incubatingObjectCount(self) -> int: ...
    def engine(self) -> QQmlEngine: ...

class QQmlListReference(PyQt6.sip.simplewrapper):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject, property: str, engine: typing.Optional[QQmlEngine] = ...) -> None: ...
    @typing.overload
    def __init__(self, a0: "QQmlListReference") -> None: ...
    @typing.overload
    def __init__(self, variant: typing.Any, engine: typing.Optional[QQmlEngine] = ...) -> None: ...
    def removeLast(self) -> bool: ...
    def replace(self, a0: int, a1: QtCore.QObject) -> bool: ...
    def canRemoveLast(self) -> bool: ...
    def canReplace(self) -> bool: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...
    def clear(self) -> bool: ...
    def at(self, a0: int) -> QtCore.QObject: ...
    def append(self, a0: QtCore.QObject) -> bool: ...
    def isReadable(self) -> bool: ...
    def isManipulable(self) -> bool: ...
    def canCount(self) -> bool: ...
    def canClear(self) -> bool: ...
    def canAt(self) -> bool: ...
    def canAppend(self) -> bool: ...
    def listElementType(self) -> QtCore.QMetaObject: ...
    def object(self) -> QtCore.QObject: ...
    def isValid(self) -> bool: ...

class QQmlNetworkAccessManagerFactory(PyQt6.sip.simplewrapper):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: "QQmlNetworkAccessManagerFactory") -> None: ...
    def create(self, parent: QtCore.QObject) -> QtNetwork.QNetworkAccessManager: ...

class QQmlParserStatus(PyQt6.sip.simplewrapper):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: "QQmlParserStatus") -> None: ...
    def componentComplete(self) -> None: ...
    def classBegin(self) -> None: ...

class QQmlProperty(PyQt6.sip.simplewrapper):
    class Type(enum.Enum):
        Invalid = ...  # type: QQmlProperty.Type
        Property = ...  # type: QQmlProperty.Type
        SignalProperty = ...  # type: QQmlProperty.Type
    class PropertyTypeCategory(enum.Enum):
        InvalidCategory = ...  # type: QQmlProperty.PropertyTypeCategory
        List = ...  # type: QQmlProperty.PropertyTypeCategory
        Object = ...  # type: QQmlProperty.PropertyTypeCategory
        Normal = ...  # type: QQmlProperty.PropertyTypeCategory
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject, a1: QQmlContext) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject, a1: QQmlEngine) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject, a1: str) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject, a1: str, a2: QQmlContext) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject, a1: str, a2: QQmlEngine) -> None: ...
    @typing.overload
    def __init__(self, a0: "QQmlProperty") -> None: ...
    def method(self) -> QtCore.QMetaMethod: ...
    def property(self) -> QtCore.QMetaProperty: ...
    def index(self) -> int: ...
    def object(self) -> QtCore.QObject: ...
    def isResettable(self) -> bool: ...
    def isDesignable(self) -> bool: ...
    def isWritable(self) -> bool: ...
    @typing.overload
    def connectNotifySignal(self, slot: PYQT_SLOT) -> bool: ...
    @typing.overload
    def connectNotifySignal(self, dest: QtCore.QObject, method: int) -> bool: ...
    def needsNotifySignal(self) -> bool: ...
    def hasNotifySignal(self) -> bool: ...
    def reset(self) -> bool: ...
    @typing.overload  # type: ignore[misc]
    def write(self, a0: typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def write(a0: QtCore.QObject, a1: str, a2: typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def write(a0: QtCore.QObject, a1: str, a2: typing.Any, a3: QQmlContext) -> bool: ...
    @typing.overload
    @staticmethod
    def write(a0: QtCore.QObject, a1: str, a2: typing.Any, a3: QQmlEngine) -> bool: ...
    @typing.overload  # type: ignore[misc]
    def read(self) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def read(a0: QtCore.QObject, a1: str) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def read(a0: QtCore.QObject, a1: str, a2: QQmlContext) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def read(a0: QtCore.QObject, a1: str, a2: QQmlEngine) -> typing.Any: ...
    def name(self) -> str: ...
    def propertyMetaType(self) -> QtCore.QMetaType: ...
    def propertyTypeName(self) -> str: ...
    def propertyTypeCategory(self) -> "QQmlProperty.PropertyTypeCategory": ...
    def propertyType(self) -> int: ...
    def isBindable(self) -> bool: ...
    def isSignalProperty(self) -> bool: ...
    def isProperty(self) -> bool: ...
    def isValid(self) -> bool: ...
    def type(self) -> "QQmlProperty.Type": ...
    def __hash__(self) -> int: ...

class QQmlPropertyMap(QtCore.QObject):
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    def updateValue(self, key: str, input: typing.Any) -> typing.Any: ...
    valueChanged: typing.ClassVar[QtCore.pyqtSignal]
    def __getitem__(self, key: str) -> typing.Any: ...
    def contains(self, key: str) -> bool: ...
    def isEmpty(self) -> bool: ...
    def __len__(self) -> int: ...
    def size(self) -> int: ...
    def count(self) -> int: ...
    def keys(self) -> typing.List[str]: ...
    def clear(self, key: str) -> None: ...
    def freeze(self) -> None: ...
    @typing.overload
    def insert(self, values: typing.Dict[str, typing.Any]) -> None: ...
    @typing.overload
    def insert(self, key: str, value: typing.Any) -> None: ...
    def value(self, key: str) -> typing.Any: ...

class QQmlPropertyValueSource(PyQt6.sip.simplewrapper):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: "QQmlPropertyValueSource") -> None: ...
    def setTarget(self, a0: QQmlProperty) -> None: ...

class QQmlScriptString(PyQt6.sip.simplewrapper):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: "QQmlScriptString") -> None: ...
    def booleanLiteral(self) -> typing.Tuple[bool, bool]: ...
    def numberLiteral(self) -> typing.Tuple[float, bool]: ...
    def stringLiteral(self) -> str: ...
    def isNullLiteral(self) -> bool: ...
    def isUndefinedLiteral(self) -> bool: ...
    def isEmpty(self) -> bool: ...

def qmlRegisterUncreatableType(a0: type, uri: str, major: int, minor: int, reason: str, qmlName: typing.Optional[str] = ...) -> int: ...
def qmlRegisterAnonymousType(a0: type, uri: str, major: int) -> int: ...
def qmlRegisterSingletonInstance(uri: str, major: int, minor: int, typeName: str, cppObject: QtCore.QObject) -> int: ...
def qmlRegisterRevision(a0: type, uri: str, major: int, minor: int, attachedProperties: type = ...) -> int: ...
def qmlAttachedPropertiesObject(a0: type, object: QtCore.QObject, create: bool = ...) -> QtCore.QObject: ...
def qjsEngine(a0: QtCore.QObject) -> QJSEngine: ...
def qmlEngine(a0: QtCore.QObject) -> QQmlEngine: ...
def qmlContext(a0: QtCore.QObject) -> QQmlContext: ...
def qmlTypeId(uri: str, versionMajor: int, versionMinor: int, qmlName: str) -> int: ...
@typing.overload
def qmlRegisterType(url: QtCore.QUrl, uri: str, versionMajor: int, versionMinor: int, qmlName: str) -> int: ...
@typing.overload
def qmlRegisterType(a0: type, uri: str, major: int, minor: int, name: typing.Optional[str] = ..., attachedProperties: type = ...) -> int: ...
@typing.overload
def qmlRegisterSingletonType(url: QtCore.QUrl, uri: str, versionMajor: int, versionMinor: int, qmlName: str) -> int: ...
@typing.overload
def qmlRegisterSingletonType(a0: type, uri: str, major: int, minor: int, factory: typing.Callable[[QQmlEngine, QJSEngine], typing.Any], name: typing.Optional[str] = ...) -> int: ...
def qmlRegisterModule(uri: str, versionMajor: int, versionMinor: int) -> None: ...
def qmlProtectModule(uri: str, majVersion: int) -> bool: ...
def qmlRegisterUncreatableMetaObject(staticMetaObject: QtCore.QMetaObject, uri: str, versionMajor: int, versionMinor: int, qmlName: str, reason: str) -> int: ...
def qmlRegisterTypeNotAvailable(uri: str, versionMajor: int, versionMinor: int, qmlName: str, message: str) -> int: ...
def qmlClearTypeRegistrations() -> None: ...
