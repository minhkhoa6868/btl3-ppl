# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0222\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\u00a5\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#")
        buf.write("\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3")
        buf.write("\65\5\65\u014a\n\65\3\65\3\65\3\65\7\65\u014f\n\65\f\65")
        buf.write("\16\65\u0152\13\65\3\65\3\65\3\65\3\65\6\65\u0158\n\65")
        buf.write("\r\65\16\65\u0159\3\65\3\65\3\65\3\65\6\65\u0160\n\65")
        buf.write("\r\65\16\65\u0161\3\65\3\65\3\65\3\65\6\65\u0168\n\65")
        buf.write("\r\65\16\65\u0169\3\65\3\65\3\65\3\65\6\65\u0170\n\65")
        buf.write("\r\65\16\65\u0171\3\65\3\65\3\65\3\65\6\65\u0178\n\65")
        buf.write("\r\65\16\65\u0179\3\65\3\65\3\65\3\65\6\65\u0180\n\65")
        buf.write("\r\65\16\65\u0181\5\65\u0184\n\65\3\66\3\66\5\66\u0188")
        buf.write("\n\66\3\66\6\66\u018b\n\66\r\66\16\66\u018c\3\67\5\67")
        buf.write("\u0190\n\67\3\67\6\67\u0193\n\67\r\67\16\67\u0194\3\67")
        buf.write("\3\67\6\67\u0199\n\67\r\67\16\67\u019a\5\67\u019d\n\67")
        buf.write("\3\67\5\67\u01a0\n\67\38\38\38\39\39\39\79\u01a8\n9\f")
        buf.write("9\169\u01ab\139\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u01b8")
        buf.write("\n:\3;\3;\3;\3;\3<\3<\7<\u01c0\n<\f<\16<\u01c3\13<\3=")
        buf.write("\3=\7=\u01c7\n=\f=\16=\u01ca\13=\3=\3=\3>\3>\3>\3>\3>")
        buf.write("\6>\u01d3\n>\r>\16>\u01d4\7>\u01d7\n>\f>\16>\u01da\13")
        buf.write(">\3>\3>\3>\3>\3>\3?\3?\3?\3@\6@\u01e5\n@\r@\16@\u01e6")
        buf.write("\3@\3@\3A\3A\3A\7A\u01ee\nA\fA\16A\u01f1\13A\3A\3A\3A")
        buf.write("\3B\3B\3B\3B\7B\u01fa\nB\fB\16B\u01fd\13B\3B\3B\3B\3C")
        buf.write("\3C\3C\3C\7C\u0206\nC\fC\16C\u0209\13C\3C\3C\3C\3C\3C")
        buf.write("\3D\3D\3D\3D\7D\u0214\nD\fD\16D\u0217\13D\3D\3D\3D\3E")
        buf.write("\3E\3E\5E\u021f\nE\3F\3F\2\2G\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62")
        buf.write("c\63e\64g\2i\65k\2m\66o\2q\67s8u9w:y;{<}=\177>\u0081?")
        buf.write("\u0083@\u0085A\u0087B\u0089C\u008bD\3\2\23\3\2\62;\3\2")
        buf.write("\63;\3\2\62\63\3\2\629\5\2\62;CHch\4\2GGgg\4\2--//\n\2")
        buf.write("$$))^^ddhhppttvv\7\2\n\n\f\f\16\17$$^^\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\4\2\f\f\17\17\4\2,,\61\61\5\2\13\13\17\17")
        buf.write("\"\"\6\2\13\f\17\17$$^^\6\2\f\f\17\17$$^^\b\2))^^hhpp")
        buf.write("ttvv\2\u024a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2i\3\2\2\2\2m\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\3\u008d\3\2\2\2\5\u00a4\3\2\2\2\7\u00a6\3\2\2\2\t\u00a9")
        buf.write("\3\2\2\2\13\u00ae\3\2\2\2\r\u00b2\3\2\2\2\17\u00b9\3\2")
        buf.write("\2\2\21\u00be\3\2\2\2\23\u00c3\3\2\2\2\25\u00ca\3\2\2")
        buf.write("\2\27\u00d4\3\2\2\2\31\u00da\3\2\2\2\33\u00de\3\2\2\2")
        buf.write("\35\u00e7\3\2\2\2\37\u00ed\3\2\2\2!\u00f3\3\2\2\2#\u00f5")
        buf.write("\3\2\2\2%\u00f7\3\2\2\2\'\u00f9\3\2\2\2)\u00fb\3\2\2\2")
        buf.write("+\u00fd\3\2\2\2-\u00ff\3\2\2\2/\u0101\3\2\2\2\61\u0103")
        buf.write("\3\2\2\2\63\u0105\3\2\2\2\65\u0107\3\2\2\2\67\u0109\3")
        buf.write("\2\2\29\u010b\3\2\2\2;\u010d\3\2\2\2=\u010f\3\2\2\2?\u0111")
        buf.write("\3\2\2\2A\u0113\3\2\2\2C\u0116\3\2\2\2E\u0119\3\2\2\2")
        buf.write("G\u011c\3\2\2\2I\u011f\3\2\2\2K\u0122\3\2\2\2M\u0125\3")
        buf.write("\2\2\2O\u0128\3\2\2\2Q\u012b\3\2\2\2S\u012d\3\2\2\2U\u0130")
        buf.write("\3\2\2\2W\u0132\3\2\2\2Y\u0135\3\2\2\2[\u0138\3\2\2\2")
        buf.write("]\u013b\3\2\2\2_\u013e\3\2\2\2a\u0140\3\2\2\2c\u0142\3")
        buf.write("\2\2\2e\u0144\3\2\2\2g\u0146\3\2\2\2i\u0149\3\2\2\2k\u0185")
        buf.write("\3\2\2\2m\u018f\3\2\2\2o\u01a1\3\2\2\2q\u01a4\3\2\2\2")
        buf.write("s\u01b7\3\2\2\2u\u01b9\3\2\2\2w\u01bd\3\2\2\2y\u01c4\3")
        buf.write("\2\2\2{\u01cd\3\2\2\2}\u01e0\3\2\2\2\177\u01e4\3\2\2\2")
        buf.write("\u0081\u01ea\3\2\2\2\u0083\u01f5\3\2\2\2\u0085\u0201\3")
        buf.write("\2\2\2\u0087\u020f\3\2\2\2\u0089\u021e\3\2\2\2\u008b\u0220")
        buf.write("\3\2\2\2\u008d\u008e\7.\2\2\u008e\4\3\2\2\2\u008f\u0090")
        buf.write("\7k\2\2\u0090\u0091\7p\2\2\u0091\u00a5\7v\2\2\u0092\u0093")
        buf.write("\7h\2\2\u0093\u0094\7n\2\2\u0094\u0095\7q\2\2\u0095\u0096")
        buf.write("\7c\2\2\u0096\u00a5\7v\2\2\u0097\u0098\7u\2\2\u0098\u0099")
        buf.write("\7v\2\2\u0099\u009a\7t\2\2\u009a\u009b\7k\2\2\u009b\u009c")
        buf.write("\7p\2\2\u009c\u00a5\7i\2\2\u009d\u009e\7d\2\2\u009e\u009f")
        buf.write("\7q\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a5\7p\2\2\u00a4\u008f")
        buf.write("\3\2\2\2\u00a4\u0092\3\2\2\2\u00a4\u0097\3\2\2\2\u00a4")
        buf.write("\u009d\3\2\2\2\u00a5\6\3\2\2\2\u00a6\u00a7\7k\2\2\u00a7")
        buf.write("\u00a8\7h\2\2\u00a8\b\3\2\2\2\u00a9\u00aa\7g\2\2\u00aa")
        buf.write("\u00ab\7n\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad\7g\2\2\u00ad")
        buf.write("\n\3\2\2\2\u00ae\u00af\7h\2\2\u00af\u00b0\7q\2\2\u00b0")
        buf.write("\u00b1\7t\2\2\u00b1\f\3\2\2\2\u00b2\u00b3\7t\2\2\u00b3")
        buf.write("\u00b4\7g\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7w\2\2\u00b6")
        buf.write("\u00b7\7t\2\2\u00b7\u00b8\7p\2\2\u00b8\16\3\2\2\2\u00b9")
        buf.write("\u00ba\7h\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc\7p\2\2\u00bc")
        buf.write("\u00bd\7e\2\2\u00bd\20\3\2\2\2\u00be\u00bf\7v\2\2\u00bf")
        buf.write("\u00c0\7{\2\2\u00c0\u00c1\7r\2\2\u00c1\u00c2\7g\2\2\u00c2")
        buf.write("\22\3\2\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5\7v\2\2\u00c5")
        buf.write("\u00c6\7t\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8\7e\2\2\u00c8")
        buf.write("\u00c9\7v\2\2\u00c9\24\3\2\2\2\u00ca\u00cb\7k\2\2\u00cb")
        buf.write("\u00cc\7p\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7g\2\2\u00ce")
        buf.write("\u00cf\7t\2\2\u00cf\u00d0\7h\2\2\u00d0\u00d1\7c\2\2\u00d1")
        buf.write("\u00d2\7e\2\2\u00d2\u00d3\7g\2\2\u00d3\26\3\2\2\2\u00d4")
        buf.write("\u00d5\7e\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7p\2\2\u00d7")
        buf.write("\u00d8\7u\2\2\u00d8\u00d9\7v\2\2\u00d9\30\3\2\2\2\u00da")
        buf.write("\u00db\7x\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd\7t\2\2\u00dd")
        buf.write("\32\3\2\2\2\u00de\u00df\7e\2\2\u00df\u00e0\7q\2\2\u00e0")
        buf.write("\u00e1\7p\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3\7k\2\2\u00e3")
        buf.write("\u00e4\7p\2\2\u00e4\u00e5\7w\2\2\u00e5\u00e6\7g\2\2\u00e6")
        buf.write("\34\3\2\2\2\u00e7\u00e8\7d\2\2\u00e8\u00e9\7t\2\2\u00e9")
        buf.write("\u00ea\7g\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7m\2\2\u00ec")
        buf.write("\36\3\2\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef\7c\2\2\u00ef")
        buf.write("\u00f0\7p\2\2\u00f0\u00f1\7i\2\2\u00f1\u00f2\7g\2\2\u00f2")
        buf.write(" \3\2\2\2\u00f3\u00f4\7\60\2\2\u00f4\"\3\2\2\2\u00f5\u00f6")
        buf.write("\7#\2\2\u00f6$\3\2\2\2\u00f7\u00f8\7=\2\2\u00f8&\3\2\2")
        buf.write("\2\u00f9\u00fa\7]\2\2\u00fa(\3\2\2\2\u00fb\u00fc\7_\2")
        buf.write("\2\u00fc*\3\2\2\2\u00fd\u00fe\7}\2\2\u00fe,\3\2\2\2\u00ff")
        buf.write("\u0100\7\177\2\2\u0100.\3\2\2\2\u0101\u0102\7*\2\2\u0102")
        buf.write("\60\3\2\2\2\u0103\u0104\7+\2\2\u0104\62\3\2\2\2\u0105")
        buf.write("\u0106\7<\2\2\u0106\64\3\2\2\2\u0107\u0108\7?\2\2\u0108")
        buf.write("\66\3\2\2\2\u0109\u010a\7-\2\2\u010a8\3\2\2\2\u010b\u010c")
        buf.write("\7/\2\2\u010c:\3\2\2\2\u010d\u010e\7,\2\2\u010e<\3\2\2")
        buf.write("\2\u010f\u0110\7\61\2\2\u0110>\3\2\2\2\u0111\u0112\7\'")
        buf.write("\2\2\u0112@\3\2\2\2\u0113\u0114\7(\2\2\u0114\u0115\7(")
        buf.write("\2\2\u0115B\3\2\2\2\u0116\u0117\7~\2\2\u0117\u0118\7~")
        buf.write("\2\2\u0118D\3\2\2\2\u0119\u011a\7-\2\2\u011a\u011b\7?")
        buf.write("\2\2\u011bF\3\2\2\2\u011c\u011d\7/\2\2\u011d\u011e\7?")
        buf.write("\2\2\u011eH\3\2\2\2\u011f\u0120\7,\2\2\u0120\u0121\7?")
        buf.write("\2\2\u0121J\3\2\2\2\u0122\u0123\7\61\2\2\u0123\u0124\7")
        buf.write("?\2\2\u0124L\3\2\2\2\u0125\u0126\7\'\2\2\u0126\u0127\7")
        buf.write("?\2\2\u0127N\3\2\2\2\u0128\u0129\7<\2\2\u0129\u012a\7")
        buf.write("?\2\2\u012aP\3\2\2\2\u012b\u012c\7>\2\2\u012cR\3\2\2\2")
        buf.write("\u012d\u012e\7>\2\2\u012e\u012f\7?\2\2\u012fT\3\2\2\2")
        buf.write("\u0130\u0131\7@\2\2\u0131V\3\2\2\2\u0132\u0133\7@\2\2")
        buf.write("\u0133\u0134\7?\2\2\u0134X\3\2\2\2\u0135\u0136\7?\2\2")
        buf.write("\u0136\u0137\7?\2\2\u0137Z\3\2\2\2\u0138\u0139\7#\2\2")
        buf.write("\u0139\u013a\7?\2\2\u013a\\\3\2\2\2\u013b\u013c\7\61\2")
        buf.write("\2\u013c\u013d\7\61\2\2\u013d^\3\2\2\2\u013e\u013f\7\13")
        buf.write("\2\2\u013f`\3\2\2\2\u0140\u0141\7\17\2\2\u0141b\3\2\2")
        buf.write("\2\u0142\u0143\7^\2\2\u0143d\3\2\2\2\u0144\u0145\7a\2")
        buf.write("\2\u0145f\3\2\2\2\u0146\u0147\t\2\2\2\u0147h\3\2\2\2\u0148")
        buf.write("\u014a\7/\2\2\u0149\u0148\3\2\2\2\u0149\u014a\3\2\2\2")
        buf.write("\u014a\u0183\3\2\2\2\u014b\u0184\7\62\2\2\u014c\u0150")
        buf.write("\t\3\2\2\u014d\u014f\5g\64\2\u014e\u014d\3\2\2\2\u014f")
        buf.write("\u0152\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151\u0184\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0154\7")
        buf.write("\62\2\2\u0154\u0155\7d\2\2\u0155\u0157\3\2\2\2\u0156\u0158")
        buf.write("\t\4\2\2\u0157\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159")
        buf.write("\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u0184\3\2\2\2")
        buf.write("\u015b\u015c\7\62\2\2\u015c\u015d\7D\2\2\u015d\u015f\3")
        buf.write("\2\2\2\u015e\u0160\t\4\2\2\u015f\u015e\3\2\2\2\u0160\u0161")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0184\3\2\2\2\u0163\u0164\7\62\2\2\u0164\u0165\7q\2\2")
        buf.write("\u0165\u0167\3\2\2\2\u0166\u0168\t\5\2\2\u0167\u0166\3")
        buf.write("\2\2\2\u0168\u0169\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a")
        buf.write("\3\2\2\2\u016a\u0184\3\2\2\2\u016b\u016c\7\62\2\2\u016c")
        buf.write("\u016d\7Q\2\2\u016d\u016f\3\2\2\2\u016e\u0170\t\5\2\2")
        buf.write("\u016f\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u016f\3")
        buf.write("\2\2\2\u0171\u0172\3\2\2\2\u0172\u0184\3\2\2\2\u0173\u0174")
        buf.write("\7\62\2\2\u0174\u0175\7z\2\2\u0175\u0177\3\2\2\2\u0176")
        buf.write("\u0178\t\6\2\2\u0177\u0176\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u0184\3")
        buf.write("\2\2\2\u017b\u017c\7\62\2\2\u017c\u017d\7Z\2\2\u017d\u017f")
        buf.write("\3\2\2\2\u017e\u0180\t\6\2\2\u017f\u017e\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182\u0184\3\2\2\2\u0183\u014b\3\2\2\2\u0183\u014c\3")
        buf.write("\2\2\2\u0183\u0153\3\2\2\2\u0183\u015b\3\2\2\2\u0183\u0163")
        buf.write("\3\2\2\2\u0183\u016b\3\2\2\2\u0183\u0173\3\2\2\2\u0183")
        buf.write("\u017b\3\2\2\2\u0184j\3\2\2\2\u0185\u0187\t\7\2\2\u0186")
        buf.write("\u0188\t\b\2\2\u0187\u0186\3\2\2\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188\u018a\3\2\2\2\u0189\u018b\5g\64\2\u018a\u0189\3")
        buf.write("\2\2\2\u018b\u018c\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018dl\3\2\2\2\u018e\u0190\7/\2\2\u018f\u018e")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0192\3\2\2\2\u0191")
        buf.write("\u0193\5g\64\2\u0192\u0191\3\2\2\2\u0193\u0194\3\2\2\2")
        buf.write("\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196\3")
        buf.write("\2\2\2\u0196\u019c\7\60\2\2\u0197\u0199\5g\64\2\u0198")
        buf.write("\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u0198\3\2\2\2")
        buf.write("\u019a\u019b\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u0198\3")
        buf.write("\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2\2\2\u019e\u01a0")
        buf.write("\5k\66\2\u019f\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("n\3\2\2\2\u01a1\u01a2\7^\2\2\u01a2\u01a3\t\t\2\2\u01a3")
        buf.write("p\3\2\2\2\u01a4\u01a9\7$\2\2\u01a5\u01a8\5o8\2\u01a6\u01a8")
        buf.write("\n\n\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8")
        buf.write("\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2")
        buf.write("\u01aa\u01ac\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ad\7")
        buf.write("$\2\2\u01adr\3\2\2\2\u01ae\u01af\7v\2\2\u01af\u01b0\7")
        buf.write("t\2\2\u01b0\u01b1\7w\2\2\u01b1\u01b8\7g\2\2\u01b2\u01b3")
        buf.write("\7h\2\2\u01b3\u01b4\7c\2\2\u01b4\u01b5\7n\2\2\u01b5\u01b6")
        buf.write("\7u\2\2\u01b6\u01b8\7g\2\2\u01b7\u01ae\3\2\2\2\u01b7\u01b2")
        buf.write("\3\2\2\2\u01b8t\3\2\2\2\u01b9\u01ba\7p\2\2\u01ba\u01bb")
        buf.write("\7k\2\2\u01bb\u01bc\7n\2\2\u01bcv\3\2\2\2\u01bd\u01c1")
        buf.write("\t\13\2\2\u01be\u01c0\t\f\2\2\u01bf\u01be\3\2\2\2\u01c0")
        buf.write("\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2")
        buf.write("\u01c2x\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c8\5]/\2")
        buf.write("\u01c5\u01c7\n\r\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01ca\3")
        buf.write("\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01cb")
        buf.write("\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\b=\2\2\u01cc")
        buf.write("z\3\2\2\2\u01cd\u01ce\7\61\2\2\u01ce\u01cf\7,\2\2\u01cf")
        buf.write("\u01d8\3\2\2\2\u01d0\u01d7\5{>\2\u01d1\u01d3\n\16\2\2")
        buf.write("\u01d2\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d2\3")
        buf.write("\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6\u01d0")
        buf.write("\3\2\2\2\u01d6\u01d2\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8")
        buf.write("\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01db\3\2\2\2")
        buf.write("\u01da\u01d8\3\2\2\2\u01db\u01dc\7,\2\2\u01dc\u01dd\7")
        buf.write("\61\2\2\u01dd\u01de\3\2\2\2\u01de\u01df\b>\2\2\u01df|")
        buf.write("\3\2\2\2\u01e0\u01e1\7\f\2\2\u01e1\u01e2\b?\3\2\u01e2")
        buf.write("~\3\2\2\2\u01e3\u01e5\t\17\2\2\u01e4\u01e3\3\2\2\2\u01e5")
        buf.write("\u01e6\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2")
        buf.write("\u01e7\u01e8\3\2\2\2\u01e8\u01e9\b@\2\2\u01e9\u0080\3")
        buf.write("\2\2\2\u01ea\u01ef\7$\2\2\u01eb\u01ee\n\20\2\2\u01ec\u01ee")
        buf.write("\5o8\2\u01ed\u01eb\3\2\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01f1")
        buf.write("\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0")
        buf.write("\u01f2\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f3\7^\2\2")
        buf.write("\u01f3\u01f4\n\t\2\2\u01f4\u0082\3\2\2\2\u01f5\u01fb\7")
        buf.write("$\2\2\u01f6\u01fa\n\21\2\2\u01f7\u01f8\7^\2\2\u01f8\u01fa")
        buf.write("\t\22\2\2\u01f9\u01f6\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa")
        buf.write("\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2")
        buf.write("\u01fc\u01fe\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe\u01ff\7")
        buf.write("\f\2\2\u01ff\u0200\bB\4\2\u0200\u0084\3\2\2\2\u0201\u0207")
        buf.write("\7$\2\2\u0202\u0206\n\21\2\2\u0203\u0204\7^\2\2\u0204")
        buf.write("\u0206\t\22\2\2\u0205\u0202\3\2\2\2\u0205\u0203\3\2\2")
        buf.write("\2\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208")
        buf.write("\3\2\2\2\u0208\u020a\3\2\2\2\u0209\u0207\3\2\2\2\u020a")
        buf.write("\u020b\7\17\2\2\u020b\u020c\7\f\2\2\u020c\u020d\3\2\2")
        buf.write("\2\u020d\u020e\bC\5\2\u020e\u0086\3\2\2\2\u020f\u0215")
        buf.write("\7$\2\2\u0210\u0214\n\21\2\2\u0211\u0212\7^\2\2\u0212")
        buf.write("\u0214\t\22\2\2\u0213\u0210\3\2\2\2\u0213\u0211\3\2\2")
        buf.write("\2\u0214\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216")
        buf.write("\3\2\2\2\u0216\u0218\3\2\2\2\u0217\u0215\3\2\2\2\u0218")
        buf.write("\u0219\7\2\2\3\u0219\u021a\bD\6\2\u021a\u0088\3\2\2\2")
        buf.write("\u021b\u021f\5\u0083B\2\u021c\u021f\5\u0085C\2\u021d\u021f")
        buf.write("\5\u0087D\2\u021e\u021b\3\2\2\2\u021e\u021c\3\2\2\2\u021e")
        buf.write("\u021d\3\2\2\2\u021f\u008a\3\2\2\2\u0220\u0221\13\2\2")
        buf.write("\2\u0221\u008c\3\2\2\2&\2\u00a4\u0149\u0150\u0159\u0161")
        buf.write("\u0169\u0171\u0179\u0181\u0183\u0187\u018c\u018f\u0194")
        buf.write("\u019a\u019c\u019f\u01a7\u01a9\u01b7\u01c1\u01c8\u01d4")
        buf.write("\u01d6\u01d8\u01e6\u01ed\u01ef\u01f9\u01fb\u0205\u0207")
        buf.write("\u0213\u0215\u021e\7\b\2\2\3?\2\3B\3\3C\4\3D\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    PRIMITIVE_TYPE = 2
    IF = 3
    ELSE = 4
    FOR = 5
    RETURN_WORD = 6
    FUNC = 7
    TYPE = 8
    STRUCT = 9
    INTERFACE = 10
    CONST = 11
    VAR = 12
    CONTINUE = 13
    BREAK = 14
    RANGE = 15
    DOT = 16
    DIFFERENT = 17
    SEMICOLON = 18
    LEFT_SQUARE_BRACKET = 19
    RIGHT_SQUARE_BRACKET = 20
    LEFT_BRACE = 21
    RIGHT_BRACE = 22
    LEFT_PARENTHESES = 23
    RIGHT_PARENTHESES = 24
    COLONS = 25
    EQUAL = 26
    PLUS = 27
    MINUS = 28
    MULTIPLY = 29
    DIVIDE = 30
    MODULO = 31
    AND = 32
    OR = 33
    PLUS_EQUAL = 34
    MINUS_EQUAL = 35
    MULTIPLY_EQUAL = 36
    DIVIDE_EQUAL = 37
    MODULO_EQUAL = 38
    COLONS_EQUAL = 39
    SMALLER = 40
    SMALLER_EQUAL = 41
    GREATER = 42
    GREATER_EQUAL = 43
    DOUBLE_EQUAL = 44
    DIFFERENT_EQUAL = 45
    COMMENT = 46
    TAB = 47
    RETURN = 48
    BACKSLASH = 49
    UNDERSCORE = 50
    INT_LITERALS = 51
    FLOAT_LITERALS = 52
    STRING_LITERALS = 53
    BOOLEAN_LITERALS = 54
    NIL = 55
    ID = 56
    SINGLE_COMMENT = 57
    MULTI_COMMENT = 58
    NL = 59
    WS = 60
    ILLEGAL_ESCAPE = 61
    END_NEWLINE = 62
    END_RETURN_NEWLINE = 63
    END_EOF = 64
    UNCLOSE_STRING = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'const'", "'var'", "'continue'", 
            "'break'", "'range'", "'.'", "'!'", "';'", "'['", "']'", "'{'", 
            "'}'", "'('", "')'", "':'", "'='", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'&&'", "'||'", "'+='", "'-='", "'*='", "'/='", "'%='", 
            "':='", "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", "'//'", 
            "'\t'", "'\r'", "'\\'", "'_'", "'nil'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "PRIMITIVE_TYPE", "IF", "ELSE", "FOR", "RETURN_WORD", "FUNC", 
            "TYPE", "STRUCT", "INTERFACE", "CONST", "VAR", "CONTINUE", "BREAK", 
            "RANGE", "DOT", "DIFFERENT", "SEMICOLON", "LEFT_SQUARE_BRACKET", 
            "RIGHT_SQUARE_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", "LEFT_PARENTHESES", 
            "RIGHT_PARENTHESES", "COLONS", "EQUAL", "PLUS", "MINUS", "MULTIPLY", 
            "DIVIDE", "MODULO", "AND", "OR", "PLUS_EQUAL", "MINUS_EQUAL", 
            "MULTIPLY_EQUAL", "DIVIDE_EQUAL", "MODULO_EQUAL", "COLONS_EQUAL", 
            "SMALLER", "SMALLER_EQUAL", "GREATER", "GREATER_EQUAL", "DOUBLE_EQUAL", 
            "DIFFERENT_EQUAL", "COMMENT", "TAB", "RETURN", "BACKSLASH", 
            "UNDERSCORE", "INT_LITERALS", "FLOAT_LITERALS", "STRING_LITERALS", 
            "BOOLEAN_LITERALS", "NIL", "ID", "SINGLE_COMMENT", "MULTI_COMMENT", 
            "NL", "WS", "ILLEGAL_ESCAPE", "END_NEWLINE", "END_RETURN_NEWLINE", 
            "END_EOF", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "PRIMITIVE_TYPE", "IF", "ELSE", "FOR", "RETURN_WORD", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "CONST", "VAR", 
                  "CONTINUE", "BREAK", "RANGE", "DOT", "DIFFERENT", "SEMICOLON", 
                  "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "LEFT_BRACE", 
                  "RIGHT_BRACE", "LEFT_PARENTHESES", "RIGHT_PARENTHESES", 
                  "COLONS", "EQUAL", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                  "MODULO", "AND", "OR", "PLUS_EQUAL", "MINUS_EQUAL", "MULTIPLY_EQUAL", 
                  "DIVIDE_EQUAL", "MODULO_EQUAL", "COLONS_EQUAL", "SMALLER", 
                  "SMALLER_EQUAL", "GREATER", "GREATER_EQUAL", "DOUBLE_EQUAL", 
                  "DIFFERENT_EQUAL", "COMMENT", "TAB", "RETURN", "BACKSLASH", 
                  "UNDERSCORE", "Digit", "INT_LITERALS", "Exponent", "FLOAT_LITERALS", 
                  "Accept_char", "STRING_LITERALS", "BOOLEAN_LITERALS", 
                  "NIL", "ID", "SINGLE_COMMENT", "MULTI_COMMENT", "NL", 
                  "WS", "ILLEGAL_ESCAPE", "END_NEWLINE", "END_RETURN_NEWLINE", 
                  "END_EOF", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    last_tk = None

    def emit(self):
        tk = self.type
        if tk not in {self.WS, self.NL}:
            self.last_tk = tk

        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();

    def handle_newline(self):
        # check next token
        next_tk = self._input.LA(1)

        while next_tk in {ord(' '), ord('\t')}:
            # move to next char
            self._input.consume()
            # check again
            next_tk = self._input.LA(1)

        if self.last_tk in {self.ID, self.INT_LITERALS, self.FLOAT_LITERALS, self.STRING_LITERALS,
                            self.CONTINUE, self.BREAK, self.RIGHT_BRACE, self.RIGHT_SQUARE_BRACKET,
                            self.RETURN_WORD, self.PRIMITIVE_TYPE, self.BOOLEAN_LITERALS}:
            if next_tk in {ord('\n'), ord('\r')} or next_tk not in {ord(';'), ord('{')}:
                self.type = self.SEMICOLON
                self.text = ";"
                return self.emit()

        if self.last_tk == self.RIGHT_PARENTHESES:
            if next_tk == self.NL:
                self._input.consume()
                next_tk = self._input.LA(1)

            while next_tk == self.WS:
                self._input.consume()
                next_tk = self._input.LA(1)

            if next_tk in {ord('+'), ord('-'), ord('*'), ord('/'), ord('%'), ord('='), ord('['), ord('(')}:
                return self.skip()

            if next_tk not in {ord(';'), ord('{')}:
                self.type = self.SEMICOLON
                self.text = ";"
                return self.emit()
        
        return self.skip()


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[61] = self.NL_action 
            actions[64] = self.END_NEWLINE_action 
            actions[65] = self.END_RETURN_NEWLINE_action 
            actions[66] = self.END_EOF_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.handle_newline() 
     

    def END_NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[:-1])
     

    def END_RETURN_NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[:-2])
     

    def END_EOF_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[:])
     


