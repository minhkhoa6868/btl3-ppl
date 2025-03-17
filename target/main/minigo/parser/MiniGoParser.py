# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u0376\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\u00a4\n\2\f\2")
        buf.write("\16\2\u00a7\13\2\3\3\3\3\3\3\3\3\3\3\3\3\7\3\u00af\n\3")
        buf.write("\f\3\16\3\u00b2\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4\u00bc\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u00c5\n\5")
        buf.write("\f\5\16\5\u00c8\13\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00d0")
        buf.write("\n\6\f\6\16\6\u00d3\13\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00db")
        buf.write("\n\7\f\7\16\7\u00de\13\7\3\b\3\b\3\b\5\b\u00e3\n\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00ee\n\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\7\n\u00f7\n\n\f\n\16\n\u00fa\13\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u0102\n\13\f\13\16")
        buf.write("\13\u0105\13\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u010d\n\f")
        buf.write("\f\f\16\f\u0110\13\f\3\r\3\r\3\r\5\r\u0115\n\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u011f\n\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\7\17\u0127\n\17\f\17\16\17\u012a")
        buf.write("\13\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u0132\n\20\f")
        buf.write("\20\16\20\u0135\13\20\3\21\3\21\3\21\3\21\3\21\3\21\7")
        buf.write("\21\u013d\n\21\f\21\16\21\u0140\13\21\3\22\3\22\3\22\5")
        buf.write("\22\u0145\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u014f\n\23\3\24\3\24\3\24\5\24\u0154\n\24\3\24\3")
        buf.write("\24\3\25\3\25\3\26\3\26\3\26\3\26\6\26\u015e\n\26\r\26")
        buf.write("\16\26\u015f\3\26\3\26\3\27\3\27\3\27\7\27\u0167\n\27")
        buf.write("\f\27\16\27\u016a\13\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\7\30\u0175\n\30\f\30\16\30\u0178\13\30")
        buf.write("\3\30\3\30\3\30\3\30\5\30\u017e\n\30\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u0184\n\31\3\32\3\32\3\32\3\32\3\32\6\32\u018b")
        buf.write("\n\32\r\32\16\32\u018c\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\5\33\u01a5\n\33\3\34\3\34\3")
        buf.write("\34\5\34\u01aa\n\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34")
        buf.write("\u01b2\n\34\f\34\16\34\u01b5\13\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\5\35\u01c9\n\35\3\36\3\36\3\36\5\36\u01ce")
        buf.write("\n\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37")
        buf.write("\u01d9\n\37\f\37\16\37\u01dc\13\37\3 \3 \3!\3!\3\"\6\"")
        buf.write("\u01e3\n\"\r\"\16\"\u01e4\3\"\3\"\3#\3#\3#\3#\3#\3#\5")
        buf.write("#\u01ef\n#\3$\3$\5$\u01f3\n$\3$\3$\3$\5$\u01f8\n$\3$\3")
        buf.write("$\5$\u01fc\n$\3$\3$\6$\u0200\n$\r$\16$\u0201\3$\3$\5$")
        buf.write("\u0206\n$\3%\3%\3%\3%\3%\5%\u020d\n%\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\5\'\u0216\n\'\3(\3(\3(\5(\u021b\n(\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\5)\u0225\n)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write("+\6+\u0231\n+\r+\16+\u0232\3+\3+\3+\3,\3,\3,\3,\3-\3-")
        buf.write("\3-\5-\u023f\n-\3.\3.\3.\3.\3.\6.\u0246\n.\r.\16.\u0247")
        buf.write("\3.\3.\3.\3/\3/\3/\5/\u0250\n/\3/\3/\5/\u0254\n/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\5\60\u025d\n\60\3\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\62\5\62\u0266\n\62\3\63\3\63\3\63")
        buf.write("\5\63\u026b\n\63\3\64\3\64\3\64\3\64\3\64\5\64\u0272\n")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u027c")
        buf.write("\n\64\3\65\3\65\3\65\5\65\u0281\n\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\38\38\58\u0290")
        buf.write("\n8\39\39\59\u0294\n9\3:\3:\3:\3:\3:\3:\5:\u029c\n:\3")
        buf.write(";\3;\3;\3;\3;\5;\u02a3\n;\3;\3;\3;\3;\5;\u02a9\n;\5;\u02ab")
        buf.write("\n;\3<\3<\3<\7<\u02b0\n<\f<\16<\u02b3\13<\3=\3=\3=\3=")
        buf.write("\3=\3=\3=\3=\3=\3=\3=\5=\u02c0\n=\3>\3>\3>\3?\3?\3?\3")
        buf.write("@\3@\3@\3@\3@\3@\6@\u02ce\n@\r@\16@\u02cf\3@\3@\5@\u02d4")
        buf.write("\n@\3@\5@\u02d7\n@\3@\5@\u02da\n@\3A\3A\3A\3A\5A\u02e0")
        buf.write("\nA\3B\3B\3B\3B\3B\3B\3B\6B\u02e9\nB\rB\16B\u02ea\3B\3")
        buf.write("B\5B\u02ef\nB\3C\3C\3C\6C\u02f4\nC\rC\16C\u02f5\3C\3C")
        buf.write("\3C\3D\3D\3D\3D\3D\3D\6D\u0301\nD\rD\16D\u0302\3D\3D\5")
        buf.write("D\u0307\nD\3D\5D\u030a\nD\3D\5D\u030d\nD\3E\3E\3E\3E\5")
        buf.write("E\u0313\nE\3F\3F\3F\3F\3F\3F\3F\6F\u031c\nF\rF\16F\u031d")
        buf.write("\3F\3F\5F\u0322\nF\3G\3G\3G\6G\u0327\nG\rG\16G\u0328\3")
        buf.write("G\3G\3G\3H\3H\3H\3H\6H\u0332\nH\rH\16H\u0333\3H\3H\3H")
        buf.write("\3H\3H\3H\3H\3H\3H\3H\3H\6H\u0341\nH\rH\16H\u0342\3H\3")
        buf.write("H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\6H\u0351\nH\rH\16H\u0352")
        buf.write("\3H\3H\3H\5H\u0358\nH\3I\3I\3J\3J\3J\5J\u035f\nJ\3K\3")
        buf.write("K\3K\3K\3K\3K\3K\3K\3K\5K\u036a\nK\3L\3L\3L\3L\3M\3M\3")
        buf.write("N\3N\3N\3N\3N\2\16\2\4\b\n\f\22\24\26\34\36 \66O\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096")
        buf.write("\u0098\u009a\2\13\3\2\35\36\3\2\37 \3\2\37!\3\2./\4\2")
        buf.write("\4\4::\3\2*/\3\2$(\4\2\24\24==\4\2\64\64::\2\u03b9\2\u009c")
        buf.write("\3\2\2\2\4\u00a8\3\2\2\2\6\u00bb\3\2\2\2\b\u00bd\3\2\2")
        buf.write("\2\n\u00c9\3\2\2\2\f\u00d4\3\2\2\2\16\u00e2\3\2\2\2\20")
        buf.write("\u00ed\3\2\2\2\22\u00ef\3\2\2\2\24\u00fb\3\2\2\2\26\u0106")
        buf.write("\3\2\2\2\30\u0114\3\2\2\2\32\u011e\3\2\2\2\34\u0120\3")
        buf.write("\2\2\2\36\u012b\3\2\2\2 \u0136\3\2\2\2\"\u0144\3\2\2\2")
        buf.write("$\u014e\3\2\2\2&\u0150\3\2\2\2(\u0157\3\2\2\2*\u015d\3")
        buf.write("\2\2\2,\u0163\3\2\2\2.\u017d\3\2\2\2\60\u0183\3\2\2\2")
        buf.write("\62\u0185\3\2\2\2\64\u01a4\3\2\2\2\66\u01a9\3\2\2\28\u01c8")
        buf.write("\3\2\2\2:\u01ca\3\2\2\2<\u01d1\3\2\2\2>\u01dd\3\2\2\2")
        buf.write("@\u01df\3\2\2\2B\u01e2\3\2\2\2D\u01ee\3\2\2\2F\u01f0\3")
        buf.write("\2\2\2H\u020c\3\2\2\2J\u020e\3\2\2\2L\u0215\3\2\2\2N\u021a")
        buf.write("\3\2\2\2P\u0224\3\2\2\2R\u0226\3\2\2\2T\u022b\3\2\2\2")
        buf.write("V\u0237\3\2\2\2X\u023e\3\2\2\2Z\u0240\3\2\2\2\\\u024c")
        buf.write("\3\2\2\2^\u025c\3\2\2\2`\u025e\3\2\2\2b\u0265\3\2\2\2")
        buf.write("d\u026a\3\2\2\2f\u027b\3\2\2\2h\u0280\3\2\2\2j\u0282\3")
        buf.write("\2\2\2l\u0288\3\2\2\2n\u028f\3\2\2\2p\u0293\3\2\2\2r\u029b")
        buf.write("\3\2\2\2t\u02aa\3\2\2\2v\u02ac\3\2\2\2x\u02bf\3\2\2\2")
        buf.write("z\u02c1\3\2\2\2|\u02c4\3\2\2\2~\u02c7\3\2\2\2\u0080\u02df")
        buf.write("\3\2\2\2\u0082\u02e1\3\2\2\2\u0084\u02f0\3\2\2\2\u0086")
        buf.write("\u02fa\3\2\2\2\u0088\u0312\3\2\2\2\u008a\u0314\3\2\2\2")
        buf.write("\u008c\u0323\3\2\2\2\u008e\u0357\3\2\2\2\u0090\u0359\3")
        buf.write("\2\2\2\u0092\u035e\3\2\2\2\u0094\u0369\3\2\2\2\u0096\u036b")
        buf.write("\3\2\2\2\u0098\u036f\3\2\2\2\u009a\u0371\3\2\2\2\u009c")
        buf.write("\u009d\b\2\1\2\u009d\u009e\5\4\3\2\u009e\u00a5\3\2\2\2")
        buf.write("\u009f\u00a0\f\4\2\2\u00a0\u00a1\5> \2\u00a1\u00a2\5\4")
        buf.write("\3\2\u00a2\u00a4\3\2\2\2\u00a3\u009f\3\2\2\2\u00a4\u00a7")
        buf.write("\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write("\3\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\b\3\1\2\u00a9")
        buf.write("\u00aa\5\6\4\2\u00aa\u00b0\3\2\2\2\u00ab\u00ac\f\4\2\2")
        buf.write("\u00ac\u00ad\7\35\2\2\u00ad\u00af\5\6\4\2\u00ae\u00ab")
        buf.write("\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\5\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3")
        buf.write("\u00bc\7\67\2\2\u00b4\u00bc\7:\2\2\u00b5\u00bc\5\66\34")
        buf.write("\2\u00b6\u00bc\5&\24\2\u00b7\u00b8\7\31\2\2\u00b8\u00b9")
        buf.write("\5\2\2\2\u00b9\u00ba\7\32\2\2\u00ba\u00bc\3\2\2\2\u00bb")
        buf.write("\u00b3\3\2\2\2\u00bb\u00b4\3\2\2\2\u00bb\u00b5\3\2\2\2")
        buf.write("\u00bb\u00b6\3\2\2\2\u00bb\u00b7\3\2\2\2\u00bc\7\3\2\2")
        buf.write("\2\u00bd\u00be\b\5\1\2\u00be\u00bf\5\n\6\2\u00bf\u00c6")
        buf.write("\3\2\2\2\u00c0\u00c1\f\4\2\2\u00c1\u00c2\5> \2\u00c2\u00c3")
        buf.write("\5\n\6\2\u00c3\u00c5\3\2\2\2\u00c4\u00c0\3\2\2\2\u00c5")
        buf.write("\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2")
        buf.write("\u00c7\t\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\b\6\1")
        buf.write("\2\u00ca\u00cb\5\f\7\2\u00cb\u00d1\3\2\2\2\u00cc\u00cd")
        buf.write("\f\4\2\2\u00cd\u00ce\t\2\2\2\u00ce\u00d0\5\f\7\2\u00cf")
        buf.write("\u00cc\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d1\u00d2\3\2\2\2\u00d2\13\3\2\2\2\u00d3\u00d1\3\2")
        buf.write("\2\2\u00d4\u00d5\b\7\1\2\u00d5\u00d6\5\16\b\2\u00d6\u00dc")
        buf.write("\3\2\2\2\u00d7\u00d8\f\4\2\2\u00d8\u00d9\t\3\2\2\u00d9")
        buf.write("\u00db\5\16\b\2\u00da\u00d7\3\2\2\2\u00db\u00de\3\2\2")
        buf.write("\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\r\3\2")
        buf.write("\2\2\u00de\u00dc\3\2\2\2\u00df\u00e0\7\36\2\2\u00e0\u00e3")
        buf.write("\5\16\b\2\u00e1\u00e3\5\20\t\2\u00e2\u00df\3\2\2\2\u00e2")
        buf.write("\u00e1\3\2\2\2\u00e3\17\3\2\2\2\u00e4\u00ee\7:\2\2\u00e5")
        buf.write("\u00ee\7\66\2\2\u00e6\u00ee\7\65\2\2\u00e7\u00ee\5\66")
        buf.write("\34\2\u00e8\u00ee\5&\24\2\u00e9\u00ea\7\31\2\2\u00ea\u00eb")
        buf.write("\5\b\5\2\u00eb\u00ec\7\32\2\2\u00ec\u00ee\3\2\2\2\u00ed")
        buf.write("\u00e4\3\2\2\2\u00ed\u00e5\3\2\2\2\u00ed\u00e6\3\2\2\2")
        buf.write("\u00ed\u00e7\3\2\2\2\u00ed\u00e8\3\2\2\2\u00ed\u00e9\3")
        buf.write("\2\2\2\u00ee\21\3\2\2\2\u00ef\u00f0\b\n\1\2\u00f0\u00f1")
        buf.write("\5\24\13\2\u00f1\u00f8\3\2\2\2\u00f2\u00f3\f\4\2\2\u00f3")
        buf.write("\u00f4\5> \2\u00f4\u00f5\5\24\13\2\u00f5\u00f7\3\2\2\2")
        buf.write("\u00f6\u00f2\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3")
        buf.write("\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\23\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fb\u00fc\b\13\1\2\u00fc\u00fd\5\26\f\2\u00fd")
        buf.write("\u0103\3\2\2\2\u00fe\u00ff\f\4\2\2\u00ff\u0100\t\2\2\2")
        buf.write("\u0100\u0102\5\26\f\2\u0101\u00fe\3\2\2\2\u0102\u0105")
        buf.write("\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104")
        buf.write("\25\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0107\b\f\1\2\u0107")
        buf.write("\u0108\5\30\r\2\u0108\u010e\3\2\2\2\u0109\u010a\f\4\2")
        buf.write("\2\u010a\u010b\t\4\2\2\u010b\u010d\5\30\r\2\u010c\u0109")
        buf.write("\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e")
        buf.write("\u010f\3\2\2\2\u010f\27\3\2\2\2\u0110\u010e\3\2\2\2\u0111")
        buf.write("\u0112\7\36\2\2\u0112\u0115\5\30\r\2\u0113\u0115\5\32")
        buf.write("\16\2\u0114\u0111\3\2\2\2\u0114\u0113\3\2\2\2\u0115\31")
        buf.write("\3\2\2\2\u0116\u011f\7:\2\2\u0117\u011f\7\65\2\2\u0118")
        buf.write("\u011f\5\66\34\2\u0119\u011f\5&\24\2\u011a\u011b\7\31")
        buf.write("\2\2\u011b\u011c\5\22\n\2\u011c\u011d\7\32\2\2\u011d\u011f")
        buf.write("\3\2\2\2\u011e\u0116\3\2\2\2\u011e\u0117\3\2\2\2\u011e")
        buf.write("\u0118\3\2\2\2\u011e\u0119\3\2\2\2\u011e\u011a\3\2\2\2")
        buf.write("\u011f\33\3\2\2\2\u0120\u0121\b\17\1\2\u0121\u0122\5\36")
        buf.write("\20\2\u0122\u0128\3\2\2\2\u0123\u0124\f\4\2\2\u0124\u0125")
        buf.write("\7#\2\2\u0125\u0127\5\36\20\2\u0126\u0123\3\2\2\2\u0127")
        buf.write("\u012a\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2")
        buf.write("\u0129\35\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u012c\b\20")
        buf.write("\1\2\u012c\u012d\5 \21\2\u012d\u0133\3\2\2\2\u012e\u012f")
        buf.write("\f\4\2\2\u012f\u0130\7\"\2\2\u0130\u0132\5 \21\2\u0131")
        buf.write("\u012e\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2")
        buf.write("\u0133\u0134\3\2\2\2\u0134\37\3\2\2\2\u0135\u0133\3\2")
        buf.write("\2\2\u0136\u0137\b\21\1\2\u0137\u0138\5\"\22\2\u0138\u013e")
        buf.write("\3\2\2\2\u0139\u013a\f\4\2\2\u013a\u013b\t\5\2\2\u013b")
        buf.write("\u013d\5\"\22\2\u013c\u0139\3\2\2\2\u013d\u0140\3\2\2")
        buf.write("\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f!\3\2")
        buf.write("\2\2\u0140\u013e\3\2\2\2\u0141\u0142\7\23\2\2\u0142\u0145")
        buf.write("\5\"\22\2\u0143\u0145\5$\23\2\u0144\u0141\3\2\2\2\u0144")
        buf.write("\u0143\3\2\2\2\u0145#\3\2\2\2\u0146\u014f\78\2\2\u0147")
        buf.write("\u014f\5\22\n\2\u0148\u014f\5\b\5\2\u0149\u014f\5\2\2")
        buf.write("\2\u014a\u014b\7\31\2\2\u014b\u014c\5\34\17\2\u014c\u014d")
        buf.write("\7\32\2\2\u014d\u014f\3\2\2\2\u014e\u0146\3\2\2\2\u014e")
        buf.write("\u0147\3\2\2\2\u014e\u0148\3\2\2\2\u014e\u0149\3\2\2\2")
        buf.write("\u014e\u014a\3\2\2\2\u014f%\3\2\2\2\u0150\u0151\5*\26")
        buf.write("\2\u0151\u0153\7\27\2\2\u0152\u0154\5,\27\2\u0153\u0152")
        buf.write("\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155\3\2\2\2\u0155")
        buf.write("\u0156\7\30\2\2\u0156\'\3\2\2\2\u0157\u0158\5\22\n\2\u0158")
        buf.write(")\3\2\2\2\u0159\u015a\7\25\2\2\u015a\u015b\5(\25\2\u015b")
        buf.write("\u015c\7\26\2\2\u015c\u015e\3\2\2\2\u015d\u0159\3\2\2")
        buf.write("\2\u015e\u015f\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160")
        buf.write("\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162\t\6\2\2\u0162")
        buf.write("+\3\2\2\2\u0163\u0168\5.\30\2\u0164\u0165\7\3\2\2\u0165")
        buf.write("\u0167\5.\30\2\u0166\u0164\3\2\2\2\u0167\u016a\3\2\2\2")
        buf.write("\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169-\3\2\2")
        buf.write("\2\u016a\u0168\3\2\2\2\u016b\u017e\5\34\17\2\u016c\u017e")
        buf.write("\5\22\n\2\u016d\u017e\5\b\5\2\u016e\u017e\5\2\2\2\u016f")
        buf.write("\u017e\5:\36\2\u0170\u0171\7\27\2\2\u0171\u0176\5.\30")
        buf.write("\2\u0172\u0173\7\3\2\2\u0173\u0175\5.\30\2\u0174\u0172")
        buf.write("\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0176")
        buf.write("\u0177\3\2\2\2\u0177\u0179\3\2\2\2\u0178\u0176\3\2\2\2")
        buf.write("\u0179\u017a\7\30\2\2\u017a\u017e\3\2\2\2\u017b\u017c")
        buf.write("\7\27\2\2\u017c\u017e\7\30\2\2\u017d\u016b\3\2\2\2\u017d")
        buf.write("\u016c\3\2\2\2\u017d\u016d\3\2\2\2\u017d\u016e\3\2\2\2")
        buf.write("\u017d\u016f\3\2\2\2\u017d\u0170\3\2\2\2\u017d\u017b\3")
        buf.write("\2\2\2\u017e/\3\2\2\2\u017f\u0184\5\34\17\2\u0180\u0184")
        buf.write("\5\22\n\2\u0181\u0184\5\b\5\2\u0182\u0184\5\2\2\2\u0183")
        buf.write("\u017f\3\2\2\2\u0183\u0180\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0183\u0182\3\2\2\2\u0184\61\3\2\2\2\u0185\u018a\5\64")
        buf.write("\33\2\u0186\u0187\7\25\2\2\u0187\u0188\5\60\31\2\u0188")
        buf.write("\u0189\7\26\2\2\u0189\u018b\3\2\2\2\u018a\u0186\3\2\2")
        buf.write("\2\u018b\u018c\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018d\63\3\2\2\2\u018e\u01a5\7:\2\2\u018f\u01a5")
        buf.write("\5t;\2\u0190\u01a5\7\65\2\2\u0191\u01a5\7\66\2\2\u0192")
        buf.write("\u01a5\7\67\2\2\u0193\u01a5\78\2\2\u0194\u0195\7\31\2")
        buf.write("\2\u0195\u0196\5\22\n\2\u0196\u0197\7\32\2\2\u0197\u01a5")
        buf.write("\3\2\2\2\u0198\u0199\7\31\2\2\u0199\u019a\5\b\5\2\u019a")
        buf.write("\u019b\7\32\2\2\u019b\u01a5\3\2\2\2\u019c\u019d\7\31\2")
        buf.write("\2\u019d\u019e\5\2\2\2\u019e\u019f\7\32\2\2\u019f\u01a5")
        buf.write("\3\2\2\2\u01a0\u01a1\7\31\2\2\u01a1\u01a2\5\34\17\2\u01a2")
        buf.write("\u01a3\7\32\2\2\u01a3\u01a5\3\2\2\2\u01a4\u018e\3\2\2")
        buf.write("\2\u01a4\u018f\3\2\2\2\u01a4\u0190\3\2\2\2\u01a4\u0191")
        buf.write("\3\2\2\2\u01a4\u0192\3\2\2\2\u01a4\u0193\3\2\2\2\u01a4")
        buf.write("\u0194\3\2\2\2\u01a4\u0198\3\2\2\2\u01a4\u019c\3\2\2\2")
        buf.write("\u01a4\u01a0\3\2\2\2\u01a5\65\3\2\2\2\u01a6\u01a7\b\34")
        buf.write("\1\2\u01a7\u01aa\5t;\2\u01a8\u01aa\58\35\2\u01a9\u01a6")
        buf.write("\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aa\u01b3\3\2\2\2\u01ab")
        buf.write("\u01ac\f\6\2\2\u01ac\u01ad\7\22\2\2\u01ad\u01b2\58\35")
        buf.write("\2\u01ae\u01af\f\5\2\2\u01af\u01b0\7\22\2\2\u01b0\u01b2")
        buf.write("\5t;\2\u01b1\u01ab\3\2\2\2\u01b1\u01ae\3\2\2\2\u01b2\u01b5")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\67\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01c9\7:\2\2\u01b7")
        buf.write("\u01c9\5\62\32\2\u01b8\u01b9\7\31\2\2\u01b9\u01ba\5\22")
        buf.write("\n\2\u01ba\u01bb\7\32\2\2\u01bb\u01c9\3\2\2\2\u01bc\u01bd")
        buf.write("\7\31\2\2\u01bd\u01be\5\b\5\2\u01be\u01bf\7\32\2\2\u01bf")
        buf.write("\u01c9\3\2\2\2\u01c0\u01c1\7\31\2\2\u01c1\u01c2\5\2\2")
        buf.write("\2\u01c2\u01c3\7\32\2\2\u01c3\u01c9\3\2\2\2\u01c4\u01c5")
        buf.write("\7\31\2\2\u01c5\u01c6\5\34\17\2\u01c6\u01c7\7\32\2\2\u01c7")
        buf.write("\u01c9\3\2\2\2\u01c8\u01b6\3\2\2\2\u01c8\u01b7\3\2\2\2")
        buf.write("\u01c8\u01b8\3\2\2\2\u01c8\u01bc\3\2\2\2\u01c8\u01c0\3")
        buf.write("\2\2\2\u01c8\u01c4\3\2\2\2\u01c99\3\2\2\2\u01ca\u01cb")
        buf.write("\7:\2\2\u01cb\u01cd\7\27\2\2\u01cc\u01ce\5<\37\2\u01cd")
        buf.write("\u01cc\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\3\2\2\2")
        buf.write("\u01cf\u01d0\7\30\2\2\u01d0;\3\2\2\2\u01d1\u01d2\7:\2")
        buf.write("\2\u01d2\u01d3\7\33\2\2\u01d3\u01da\5x=\2\u01d4\u01d5")
        buf.write("\7\3\2\2\u01d5\u01d6\7:\2\2\u01d6\u01d7\7\33\2\2\u01d7")
        buf.write("\u01d9\5x=\2\u01d8\u01d4\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da")
        buf.write("\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db=\3\2\2\2\u01dc")
        buf.write("\u01da\3\2\2\2\u01dd\u01de\t\7\2\2\u01de?\3\2\2\2\u01df")
        buf.write("\u01e0\t\b\2\2\u01e0A\3\2\2\2\u01e1\u01e3\5D#\2\u01e2")
        buf.write("\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e2\3\2\2\2")
        buf.write("\u01e4\u01e5\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7\7")
        buf.write("\2\2\3\u01e7C\3\2\2\2\u01e8\u01ef\5f\64\2\u01e9\u01ef")
        buf.write("\5j\66\2\u01ea\u01ef\5l\67\2\u01eb\u01ef\5F$\2\u01ec\u01ef")
        buf.write("\5T+\2\u01ed\u01ef\5Z.\2\u01ee\u01e8\3\2\2\2\u01ee\u01e9")
        buf.write("\3\2\2\2\u01ee\u01ea\3\2\2\2\u01ee\u01eb\3\2\2\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ed\3\2\2\2\u01efE\3\2\2\2\u01f0")
        buf.write("\u01f2\7\t\2\2\u01f1\u01f3\5R*\2\u01f2\u01f1\3\2\2\2\u01f2")
        buf.write("\u01f3\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f5\7:\2\2")
        buf.write("\u01f5\u01f7\7\31\2\2\u01f6\u01f8\5H%\2\u01f7\u01f6\3")
        buf.write("\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fb")
        buf.write("\7\32\2\2\u01fa\u01fc\5N(\2\u01fb\u01fa\3\2\2\2\u01fb")
        buf.write("\u01fc\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01ff\7\27\2")
        buf.write("\2\u01fe\u0200\5P)\2\u01ff\u01fe\3\2\2\2\u0200\u0201\3")
        buf.write("\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0203")
        buf.write("\3\2\2\2\u0203\u0205\7\30\2\2\u0204\u0206\7\24\2\2\u0205")
        buf.write("\u0204\3\2\2\2\u0205\u0206\3\2\2\2\u0206G\3\2\2\2\u0207")
        buf.write("\u0208\5J&\2\u0208\u0209\7\3\2\2\u0209\u020a\5H%\2\u020a")
        buf.write("\u020d\3\2\2\2\u020b\u020d\5J&\2\u020c\u0207\3\2\2\2\u020c")
        buf.write("\u020b\3\2\2\2\u020dI\3\2\2\2\u020e\u020f\5L\'\2\u020f")
        buf.write("\u0210\5N(\2\u0210K\3\2\2\2\u0211\u0212\7:\2\2\u0212\u0213")
        buf.write("\7\3\2\2\u0213\u0216\5L\'\2\u0214\u0216\7:\2\2\u0215\u0211")
        buf.write("\3\2\2\2\u0215\u0214\3\2\2\2\u0216M\3\2\2\2\u0217\u021b")
        buf.write("\7\4\2\2\u0218\u021b\7:\2\2\u0219\u021b\5*\26\2\u021a")
        buf.write("\u0217\3\2\2\2\u021a\u0218\3\2\2\2\u021a\u0219\3\2\2\2")
        buf.write("\u021bO\3\2\2\2\u021c\u0225\5f\64\2\u021d\u0225\5j\66")
        buf.write("\2\u021e\u0225\5l\67\2\u021f\u0225\5r:\2\u0220\u0225\5")
        buf.write("~@\2\u0221\u0225\5\u008eH\2\u0222\u0225\5\66\34\2\u0223")
        buf.write("\u0225\5F$\2\u0224\u021c\3\2\2\2\u0224\u021d\3\2\2\2\u0224")
        buf.write("\u021e\3\2\2\2\u0224\u021f\3\2\2\2\u0224\u0220\3\2\2\2")
        buf.write("\u0224\u0221\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0223\3")
        buf.write("\2\2\2\u0225Q\3\2\2\2\u0226\u0227\7\31\2\2\u0227\u0228")
        buf.write("\7:\2\2\u0228\u0229\7:\2\2\u0229\u022a\7\32\2\2\u022a")
        buf.write("S\3\2\2\2\u022b\u022c\7\n\2\2\u022c\u022d\7:\2\2\u022d")
        buf.write("\u022e\7\13\2\2\u022e\u0230\7\27\2\2\u022f\u0231\5V,\2")
        buf.write("\u0230\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0230\3")
        buf.write("\2\2\2\u0232\u0233\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0235")
        buf.write("\7\30\2\2\u0235\u0236\t\t\2\2\u0236U\3\2\2\2\u0237\u0238")
        buf.write("\7:\2\2\u0238\u0239\5X-\2\u0239\u023a\t\t\2\2\u023aW\3")
        buf.write("\2\2\2\u023b\u023f\7\4\2\2\u023c\u023f\7:\2\2\u023d\u023f")
        buf.write("\5*\26\2\u023e\u023b\3\2\2\2\u023e\u023c\3\2\2\2\u023e")
        buf.write("\u023d\3\2\2\2\u023fY\3\2\2\2\u0240\u0241\7\n\2\2\u0241")
        buf.write("\u0242\7:\2\2\u0242\u0243\7\f\2\2\u0243\u0245\7\27\2\2")
        buf.write("\u0244\u0246\5\\/\2\u0245\u0244\3\2\2\2\u0246\u0247\3")
        buf.write("\2\2\2\u0247\u0245\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u0249")
        buf.write("\3\2\2\2\u0249\u024a\7\30\2\2\u024a\u024b\t\t\2\2\u024b")
        buf.write("[\3\2\2\2\u024c\u024d\7:\2\2\u024d\u024f\7\31\2\2\u024e")
        buf.write("\u0250\5^\60\2\u024f\u024e\3\2\2\2\u024f\u0250\3\2\2\2")
        buf.write("\u0250\u0251\3\2\2\2\u0251\u0253\7\32\2\2\u0252\u0254")
        buf.write("\5d\63\2\u0253\u0252\3\2\2\2\u0253\u0254\3\2\2\2\u0254")
        buf.write("\u0255\3\2\2\2\u0255\u0256\t\t\2\2\u0256]\3\2\2\2\u0257")
        buf.write("\u0258\5`\61\2\u0258\u0259\7\3\2\2\u0259\u025a\5^\60\2")
        buf.write("\u025a\u025d\3\2\2\2\u025b\u025d\5`\61\2\u025c\u0257\3")
        buf.write("\2\2\2\u025c\u025b\3\2\2\2\u025d_\3\2\2\2\u025e\u025f")
        buf.write("\5b\62\2\u025f\u0260\5d\63\2\u0260a\3\2\2\2\u0261\u0262")
        buf.write("\7:\2\2\u0262\u0263\7\3\2\2\u0263\u0266\5b\62\2\u0264")
        buf.write("\u0266\7:\2\2\u0265\u0261\3\2\2\2\u0265\u0264\3\2\2\2")
        buf.write("\u0266c\3\2\2\2\u0267\u026b\7\4\2\2\u0268\u026b\7:\2\2")
        buf.write("\u0269\u026b\5*\26\2\u026a\u0267\3\2\2\2\u026a\u0268\3")
        buf.write("\2\2\2\u026a\u0269\3\2\2\2\u026be\3\2\2\2\u026c\u026d")
        buf.write("\7\16\2\2\u026d\u026e\7:\2\2\u026e\u0271\5h\65\2\u026f")
        buf.write("\u0270\7\34\2\2\u0270\u0272\5x=\2\u0271\u026f\3\2\2\2")
        buf.write("\u0271\u0272\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0274\t")
        buf.write("\t\2\2\u0274\u027c\3\2\2\2\u0275\u0276\7\16\2\2\u0276")
        buf.write("\u0277\7:\2\2\u0277\u0278\7\34\2\2\u0278\u0279\5x=\2\u0279")
        buf.write("\u027a\t\t\2\2\u027a\u027c\3\2\2\2\u027b\u026c\3\2\2\2")
        buf.write("\u027b\u0275\3\2\2\2\u027cg\3\2\2\2\u027d\u0281\7\4\2")
        buf.write("\2\u027e\u0281\5*\26\2\u027f\u0281\7:\2\2\u0280\u027d")
        buf.write("\3\2\2\2\u0280\u027e\3\2\2\2\u0280\u027f\3\2\2\2\u0281")
        buf.write("i\3\2\2\2\u0282\u0283\7\r\2\2\u0283\u0284\7:\2\2\u0284")
        buf.write("\u0285\7\34\2\2\u0285\u0286\5x=\2\u0286\u0287\t\t\2\2")
        buf.write("\u0287k\3\2\2\2\u0288\u0289\5n8\2\u0289\u028a\5p9\2\u028a")
        buf.write("\u028b\5x=\2\u028b\u028c\t\t\2\2\u028cm\3\2\2\2\u028d")
        buf.write("\u0290\7:\2\2\u028e\u0290\5\66\34\2\u028f\u028d\3\2\2")
        buf.write("\2\u028f\u028e\3\2\2\2\u0290o\3\2\2\2\u0291\u0294\5@!")
        buf.write("\2\u0292\u0294\7)\2\2\u0293\u0291\3\2\2\2\u0293\u0292")
        buf.write("\3\2\2\2\u0294q\3\2\2\2\u0295\u0296\7\b\2\2\u0296\u0297")
        buf.write("\5x=\2\u0297\u0298\t\t\2\2\u0298\u029c\3\2\2\2\u0299\u029a")
        buf.write("\7\b\2\2\u029a\u029c\t\t\2\2\u029b\u0295\3\2\2\2\u029b")
        buf.write("\u0299\3\2\2\2\u029cs\3\2\2\2\u029d\u029e\7:\2\2\u029e")
        buf.write("\u029f\7\31\2\2\u029f\u02a0\5v<\2\u02a0\u02a2\7\32\2\2")
        buf.write("\u02a1\u02a3\7\24\2\2\u02a2\u02a1\3\2\2\2\u02a2\u02a3")
        buf.write("\3\2\2\2\u02a3\u02ab\3\2\2\2\u02a4\u02a5\7:\2\2\u02a5")
        buf.write("\u02a6\7\31\2\2\u02a6\u02a8\7\32\2\2\u02a7\u02a9\7\24")
        buf.write("\2\2\u02a8\u02a7\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02ab")
        buf.write("\3\2\2\2\u02aa\u029d\3\2\2\2\u02aa\u02a4\3\2\2\2\u02ab")
        buf.write("u\3\2\2\2\u02ac\u02b1\5x=\2\u02ad\u02ae\7\3\2\2\u02ae")
        buf.write("\u02b0\5x=\2\u02af\u02ad\3\2\2\2\u02b0\u02b3\3\2\2\2\u02b1")
        buf.write("\u02af\3\2\2\2\u02b1\u02b2\3\2\2\2\u02b2w\3\2\2\2\u02b3")
        buf.write("\u02b1\3\2\2\2\u02b4\u02c0\5:\36\2\u02b5\u02c0\79\2\2")
        buf.write("\u02b6\u02c0\5\34\17\2\u02b7\u02c0\5&\24\2\u02b8\u02c0")
        buf.write("\5\22\n\2\u02b9\u02c0\5\b\5\2\u02ba\u02c0\5\2\2\2\u02bb")
        buf.write("\u02bc\7\31\2\2\u02bc\u02bd\5x=\2\u02bd\u02be\7\32\2\2")
        buf.write("\u02be\u02c0\3\2\2\2\u02bf\u02b4\3\2\2\2\u02bf\u02b5\3")
        buf.write("\2\2\2\u02bf\u02b6\3\2\2\2\u02bf\u02b7\3\2\2\2\u02bf\u02b8")
        buf.write("\3\2\2\2\u02bf\u02b9\3\2\2\2\u02bf\u02ba\3\2\2\2\u02bf")
        buf.write("\u02bb\3\2\2\2\u02c0y\3\2\2\2\u02c1\u02c2\7\20\2\2\u02c2")
        buf.write("\u02c3\t\t\2\2\u02c3{\3\2\2\2\u02c4\u02c5\7\17\2\2\u02c5")
        buf.write("\u02c6\t\t\2\2\u02c6}\3\2\2\2\u02c7\u02c8\7\5\2\2\u02c8")
        buf.write("\u02c9\7\31\2\2\u02c9\u02ca\5\34\17\2\u02ca\u02cb\7\32")
        buf.write("\2\2\u02cb\u02cd\7\27\2\2\u02cc\u02ce\5P)\2\u02cd\u02cc")
        buf.write("\3\2\2\2\u02ce\u02cf\3\2\2\2\u02cf\u02cd\3\2\2\2\u02cf")
        buf.write("\u02d0\3\2\2\2\u02d0\u02d1\3\2\2\2\u02d1\u02d3\7\30\2")
        buf.write("\2\u02d2\u02d4\7\24\2\2\u02d3\u02d2\3\2\2\2\u02d3\u02d4")
        buf.write("\3\2\2\2\u02d4\u02d6\3\2\2\2\u02d5\u02d7\5\u0080A\2\u02d6")
        buf.write("\u02d5\3\2\2\2\u02d6\u02d7\3\2\2\2\u02d7\u02d9\3\2\2\2")
        buf.write("\u02d8\u02da\5\u0084C\2\u02d9\u02d8\3\2\2\2\u02d9\u02da")
        buf.write("\3\2\2\2\u02da\177\3\2\2\2\u02db\u02dc\5\u0082B\2\u02dc")
        buf.write("\u02dd\5\u0080A\2\u02dd\u02e0\3\2\2\2\u02de\u02e0\5\u0082")
        buf.write("B\2\u02df\u02db\3\2\2\2\u02df\u02de\3\2\2\2\u02e0\u0081")
        buf.write("\3\2\2\2\u02e1\u02e2\7\6\2\2\u02e2\u02e3\7\5\2\2\u02e3")
        buf.write("\u02e4\7\31\2\2\u02e4\u02e5\5\34\17\2\u02e5\u02e6\7\32")
        buf.write("\2\2\u02e6\u02e8\7\27\2\2\u02e7\u02e9\5P)\2\u02e8\u02e7")
        buf.write("\3\2\2\2\u02e9\u02ea\3\2\2\2\u02ea\u02e8\3\2\2\2\u02ea")
        buf.write("\u02eb\3\2\2\2\u02eb\u02ec\3\2\2\2\u02ec\u02ee\7\30\2")
        buf.write("\2\u02ed\u02ef\7\24\2\2\u02ee\u02ed\3\2\2\2\u02ee\u02ef")
        buf.write("\3\2\2\2\u02ef\u0083\3\2\2\2\u02f0\u02f1\7\6\2\2\u02f1")
        buf.write("\u02f3\7\27\2\2\u02f2\u02f4\5P)\2\u02f3\u02f2\3\2\2\2")
        buf.write("\u02f4\u02f5\3\2\2\2\u02f5\u02f3\3\2\2\2\u02f5\u02f6\3")
        buf.write("\2\2\2\u02f6\u02f7\3\2\2\2\u02f7\u02f8\7\30\2\2\u02f8")
        buf.write("\u02f9\t\t\2\2\u02f9\u0085\3\2\2\2\u02fa\u02fb\7\5\2\2")
        buf.write("\u02fb\u02fc\7\31\2\2\u02fc\u02fd\5\34\17\2\u02fd\u02fe")
        buf.write("\7\32\2\2\u02fe\u0300\7\27\2\2\u02ff\u0301\5\u0094K\2")
        buf.write("\u0300\u02ff\3\2\2\2\u0301\u0302\3\2\2\2\u0302\u0300\3")
        buf.write("\2\2\2\u0302\u0303\3\2\2\2\u0303\u0304\3\2\2\2\u0304\u0306")
        buf.write("\7\30\2\2\u0305\u0307\7\24\2\2\u0306\u0305\3\2\2\2\u0306")
        buf.write("\u0307\3\2\2\2\u0307\u0309\3\2\2\2\u0308\u030a\5\u0088")
        buf.write("E\2\u0309\u0308\3\2\2\2\u0309\u030a\3\2\2\2\u030a\u030c")
        buf.write("\3\2\2\2\u030b\u030d\5\u008cG\2\u030c\u030b\3\2\2\2\u030c")
        buf.write("\u030d\3\2\2\2\u030d\u0087\3\2\2\2\u030e\u030f\5\u008a")
        buf.write("F\2\u030f\u0310\5\u0088E\2\u0310\u0313\3\2\2\2\u0311\u0313")
        buf.write("\5\u008aF\2\u0312\u030e\3\2\2\2\u0312\u0311\3\2\2\2\u0313")
        buf.write("\u0089\3\2\2\2\u0314\u0315\7\6\2\2\u0315\u0316\7\5\2\2")
        buf.write("\u0316\u0317\7\31\2\2\u0317\u0318\5\34\17\2\u0318\u0319")
        buf.write("\7\32\2\2\u0319\u031b\7\27\2\2\u031a\u031c\5\u0094K\2")
        buf.write("\u031b\u031a\3\2\2\2\u031c\u031d\3\2\2\2\u031d\u031b\3")
        buf.write("\2\2\2\u031d\u031e\3\2\2\2\u031e\u031f\3\2\2\2\u031f\u0321")
        buf.write("\7\30\2\2\u0320\u0322\7\24\2\2\u0321\u0320\3\2\2\2\u0321")
        buf.write("\u0322\3\2\2\2\u0322\u008b\3\2\2\2\u0323\u0324\7\6\2\2")
        buf.write("\u0324\u0326\7\27\2\2\u0325\u0327\5\u0094K\2\u0326\u0325")
        buf.write("\3\2\2\2\u0327\u0328\3\2\2\2\u0328\u0326\3\2\2\2\u0328")
        buf.write("\u0329\3\2\2\2\u0329\u032a\3\2\2\2\u032a\u032b\7\30\2")
        buf.write("\2\u032b\u032c\t\t\2\2\u032c\u008d\3\2\2\2\u032d\u032e")
        buf.write("\7\7\2\2\u032e\u032f\5\u0098M\2\u032f\u0331\7\27\2\2\u0330")
        buf.write("\u0332\5\u0094K\2\u0331\u0330\3\2\2\2\u0332\u0333\3\2")
        buf.write("\2\2\u0333\u0331\3\2\2\2\u0333\u0334\3\2\2\2\u0334\u0335")
        buf.write("\3\2\2\2\u0335\u0336\7\30\2\2\u0336\u0337\t\t\2\2\u0337")
        buf.write("\u0358\3\2\2\2\u0338\u0339\7\7\2\2\u0339\u033a\5\u0096")
        buf.write("L\2\u033a\u033b\7\24\2\2\u033b\u033c\5\u0098M\2\u033c")
        buf.write("\u033d\7\24\2\2\u033d\u033e\5\u009aN\2\u033e\u0340\7\27")
        buf.write("\2\2\u033f\u0341\5\u0094K\2\u0340\u033f\3\2\2\2\u0341")
        buf.write("\u0342\3\2\2\2\u0342\u0340\3\2\2\2\u0342\u0343\3\2\2\2")
        buf.write("\u0343\u0344\3\2\2\2\u0344\u0345\7\30\2\2\u0345\u0346")
        buf.write("\t\t\2\2\u0346\u0358\3\2\2\2\u0347\u0348\7\7\2\2\u0348")
        buf.write("\u0349\5\u0090I\2\u0349\u034a\7\3\2\2\u034a\u034b\5\u0090")
        buf.write("I\2\u034b\u034c\7)\2\2\u034c\u034d\7\21\2\2\u034d\u034e")
        buf.write("\5\u0092J\2\u034e\u0350\7\27\2\2\u034f\u0351\5\u0094K")
        buf.write("\2\u0350\u034f\3\2\2\2\u0351\u0352\3\2\2\2\u0352\u0350")
        buf.write("\3\2\2\2\u0352\u0353\3\2\2\2\u0353\u0354\3\2\2\2\u0354")
        buf.write("\u0355\7\30\2\2\u0355\u0356\t\t\2\2\u0356\u0358\3\2\2")
        buf.write("\2\u0357\u032d\3\2\2\2\u0357\u0338\3\2\2\2\u0357\u0347")
        buf.write("\3\2\2\2\u0358\u008f\3\2\2\2\u0359\u035a\t\n\2\2\u035a")
        buf.write("\u0091\3\2\2\2\u035b\u035f\7:\2\2\u035c\u035f\5&\24\2")
        buf.write("\u035d\u035f\5\66\34\2\u035e\u035b\3\2\2\2\u035e\u035c")
        buf.write("\3\2\2\2\u035e\u035d\3\2\2\2\u035f\u0093\3\2\2\2\u0360")
        buf.write("\u036a\5f\64\2\u0361\u036a\5j\66\2\u0362\u036a\5l\67\2")
        buf.write("\u0363\u036a\5r:\2\u0364\u036a\5\u0086D\2\u0365\u036a")
        buf.write("\5z>\2\u0366\u036a\5|?\2\u0367\u036a\5\u008eH\2\u0368")
        buf.write("\u036a\5\66\34\2\u0369\u0360\3\2\2\2\u0369\u0361\3\2\2")
        buf.write("\2\u0369\u0362\3\2\2\2\u0369\u0363\3\2\2\2\u0369\u0364")
        buf.write("\3\2\2\2\u0369\u0365\3\2\2\2\u0369\u0366\3\2\2\2\u0369")
        buf.write("\u0367\3\2\2\2\u0369\u0368\3\2\2\2\u036a\u0095\3\2\2\2")
        buf.write("\u036b\u036c\7:\2\2\u036c\u036d\7)\2\2\u036d\u036e\5x")
        buf.write("=\2\u036e\u0097\3\2\2\2\u036f\u0370\5\34\17\2\u0370\u0099")
        buf.write("\3\2\2\2\u0371\u0372\7:\2\2\u0372\u0373\5@!\2\u0373\u0374")
        buf.write("\5x=\2\u0374\u009b\3\2\2\2V\u00a5\u00b0\u00bb\u00c6\u00d1")
        buf.write("\u00dc\u00e2\u00ed\u00f8\u0103\u010e\u0114\u011e\u0128")
        buf.write("\u0133\u013e\u0144\u014e\u0153\u015f\u0168\u0176\u017d")
        buf.write("\u0183\u018c\u01a4\u01a9\u01b1\u01b3\u01c8\u01cd\u01da")
        buf.write("\u01e4\u01ee\u01f2\u01f7\u01fb\u0201\u0205\u020c\u0215")
        buf.write("\u021a\u0224\u0232\u023e\u0247\u024f\u0253\u025c\u0265")
        buf.write("\u026a\u0271\u027b\u0280\u028f\u0293\u029b\u02a2\u02a8")
        buf.write("\u02aa\u02b1\u02bf\u02cf\u02d3\u02d6\u02d9\u02df\u02ea")
        buf.write("\u02ee\u02f5\u0302\u0306\u0309\u030c\u0312\u031d\u0321")
        buf.write("\u0328\u0333\u0342\u0352\u0357\u035e\u0369")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "<INVALID>", "'if'", "'else'", 
                     "'for'", "'return'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'.'", "'!'", "';'", "'['", "']'", "'{'", 
                     "'}'", "'('", "')'", "':'", "'='", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'&&'", "'||'", "'+='", "'-='", "'*='", 
                     "'/='", "'%='", "':='", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'!='", "'//'", "'\t'", "'\r'", "'\\'", "'_'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'nil'", "<INVALID>", "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "PRIMITIVE_TYPE", "IF", 
                      "ELSE", "FOR", "RETURN_WORD", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "CONST", "VAR", "CONTINUE", "BREAK", 
                      "RANGE", "DOT", "DIFFERENT", "SEMICOLON", "LEFT_SQUARE_BRACKET", 
                      "RIGHT_SQUARE_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
                      "LEFT_PARENTHESES", "RIGHT_PARENTHESES", "COLONS", 
                      "EQUAL", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", 
                      "AND", "OR", "PLUS_EQUAL", "MINUS_EQUAL", "MULTIPLY_EQUAL", 
                      "DIVIDE_EQUAL", "MODULO_EQUAL", "COLONS_EQUAL", "SMALLER", 
                      "SMALLER_EQUAL", "GREATER", "GREATER_EQUAL", "DOUBLE_EQUAL", 
                      "DIFFERENT_EQUAL", "COMMENT", "TAB", "RETURN", "BACKSLASH", 
                      "UNDERSCORE", "INT_LITERALS", "FLOAT_LITERALS", "STRING_LITERALS", 
                      "BOOLEAN_LITERALS", "NIL", "ID", "SINGLE_COMMENT", 
                      "MULTI_COMMENT", "NL", "WS", "ILLEGAL_ESCAPE", "END_NEWLINE", 
                      "END_RETURN_NEWLINE", "END_EOF", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

    RULE_expression_string = 0
    RULE_plus_string = 1
    RULE_term_plus = 2
    RULE_expression_float = 3
    RULE_add_float = 4
    RULE_mul_float = 5
    RULE_unary_float = 6
    RULE_term_float = 7
    RULE_expression_int = 8
    RULE_add_int = 9
    RULE_mul_int = 10
    RULE_unary_int = 11
    RULE_term_int = 12
    RULE_expression_boolean = 13
    RULE_and_boolean = 14
    RULE_compare_boolean = 15
    RULE_unary_boolean = 16
    RULE_term_boolean = 17
    RULE_expression_array = 18
    RULE_array_size = 19
    RULE_arrays_type = 20
    RULE_array_instance = 21
    RULE_array_value = 22
    RULE_array_idx = 23
    RULE_array_access_field = 24
    RULE_arr_name = 25
    RULE_access_field = 26
    RULE_field = 27
    RULE_struct_value = 28
    RULE_field_value = 29
    RULE_relational = 30
    RULE_other_operations = 31
    RULE_program = 32
    RULE_decl = 33
    RULE_funcdecl = 34
    RULE_funcParams = 35
    RULE_funcParam = 36
    RULE_funcListName = 37
    RULE_funcType = 38
    RULE_block = 39
    RULE_receiver = 40
    RULE_structdecl = 41
    RULE_struct_field = 42
    RULE_struct_fieldType = 43
    RULE_interfacedecl = 44
    RULE_interface_field = 45
    RULE_interfaceParams = 46
    RULE_interfaceParam = 47
    RULE_interfaceListName = 48
    RULE_interfaceType = 49
    RULE_vardecl = 50
    RULE_varType = 51
    RULE_constdecl = 52
    RULE_shortvardecl = 53
    RULE_lhs = 54
    RULE_assign_operators = 55
    RULE_returndecl = 56
    RULE_callfuncdecl = 57
    RULE_argu_list = 58
    RULE_value_assign = 59
    RULE_breakdecl = 60
    RULE_continuedecl = 61
    RULE_ifelsedecl = 62
    RULE_elifdecls = 63
    RULE_elifdecl = 64
    RULE_elsedecl = 65
    RULE_ifelsedecl_inside_loop = 66
    RULE_elifdecls_inside_loop = 67
    RULE_elifdecl_inside_loop = 68
    RULE_elsedecl_inside_loop = 69
    RULE_forloopdecl = 70
    RULE_for_access_value = 71
    RULE_for_arr = 72
    RULE_block_inside_loop = 73
    RULE_initialization = 74
    RULE_condition = 75
    RULE_update = 76

    ruleNames =  [ "expression_string", "plus_string", "term_plus", "expression_float", 
                   "add_float", "mul_float", "unary_float", "term_float", 
                   "expression_int", "add_int", "mul_int", "unary_int", 
                   "term_int", "expression_boolean", "and_boolean", "compare_boolean", 
                   "unary_boolean", "term_boolean", "expression_array", 
                   "array_size", "arrays_type", "array_instance", "array_value", 
                   "array_idx", "array_access_field", "arr_name", "access_field", 
                   "field", "struct_value", "field_value", "relational", 
                   "other_operations", "program", "decl", "funcdecl", "funcParams", 
                   "funcParam", "funcListName", "funcType", "block", "receiver", 
                   "structdecl", "struct_field", "struct_fieldType", "interfacedecl", 
                   "interface_field", "interfaceParams", "interfaceParam", 
                   "interfaceListName", "interfaceType", "vardecl", "varType", 
                   "constdecl", "shortvardecl", "lhs", "assign_operators", 
                   "returndecl", "callfuncdecl", "argu_list", "value_assign", 
                   "breakdecl", "continuedecl", "ifelsedecl", "elifdecls", 
                   "elifdecl", "elsedecl", "ifelsedecl_inside_loop", "elifdecls_inside_loop", 
                   "elifdecl_inside_loop", "elsedecl_inside_loop", "forloopdecl", 
                   "for_access_value", "for_arr", "block_inside_loop", "initialization", 
                   "condition", "update" ]

    EOF = Token.EOF
    T__0=1
    PRIMITIVE_TYPE=2
    IF=3
    ELSE=4
    FOR=5
    RETURN_WORD=6
    FUNC=7
    TYPE=8
    STRUCT=9
    INTERFACE=10
    CONST=11
    VAR=12
    CONTINUE=13
    BREAK=14
    RANGE=15
    DOT=16
    DIFFERENT=17
    SEMICOLON=18
    LEFT_SQUARE_BRACKET=19
    RIGHT_SQUARE_BRACKET=20
    LEFT_BRACE=21
    RIGHT_BRACE=22
    LEFT_PARENTHESES=23
    RIGHT_PARENTHESES=24
    COLONS=25
    EQUAL=26
    PLUS=27
    MINUS=28
    MULTIPLY=29
    DIVIDE=30
    MODULO=31
    AND=32
    OR=33
    PLUS_EQUAL=34
    MINUS_EQUAL=35
    MULTIPLY_EQUAL=36
    DIVIDE_EQUAL=37
    MODULO_EQUAL=38
    COLONS_EQUAL=39
    SMALLER=40
    SMALLER_EQUAL=41
    GREATER=42
    GREATER_EQUAL=43
    DOUBLE_EQUAL=44
    DIFFERENT_EQUAL=45
    COMMENT=46
    TAB=47
    RETURN=48
    BACKSLASH=49
    UNDERSCORE=50
    INT_LITERALS=51
    FLOAT_LITERALS=52
    STRING_LITERALS=53
    BOOLEAN_LITERALS=54
    NIL=55
    ID=56
    SINGLE_COMMENT=57
    MULTI_COMMENT=58
    NL=59
    WS=60
    ILLEGAL_ESCAPE=61
    END_NEWLINE=62
    END_RETURN_NEWLINE=63
    END_EOF=64
    UNCLOSE_STRING=65
    ERROR_CHAR=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Expression_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def plus_string(self):
            return self.getTypedRuleContext(MiniGoParser.Plus_stringContext,0)


        def expression_string(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_stringContext,0)


        def relational(self):
            return self.getTypedRuleContext(MiniGoParser.RelationalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_string" ):
                return visitor.visitExpression_string(self)
            else:
                return visitor.visitChildren(self)



    def expression_string(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression_stringContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression_string, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.plus_string(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 163
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression_stringContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_string)
                    self.state = 157
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 158
                    self.relational()
                    self.state = 159
                    self.plus_string(0) 
                self.state = 165
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Plus_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term_plus(self):
            return self.getTypedRuleContext(MiniGoParser.Term_plusContext,0)


        def plus_string(self):
            return self.getTypedRuleContext(MiniGoParser.Plus_stringContext,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_plus_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlus_string" ):
                return visitor.visitPlus_string(self)
            else:
                return visitor.visitChildren(self)



    def plus_string(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Plus_stringContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_plus_string, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.term_plus()
            self._ctx.stop = self._input.LT(-1)
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Plus_stringContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_plus_string)
                    self.state = 169
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 170
                    self.match(MiniGoParser.PLUS)
                    self.state = 171
                    self.term_plus() 
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term_plusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERALS(self):
            return self.getToken(MiniGoParser.STRING_LITERALS, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def access_field(self):
            return self.getTypedRuleContext(MiniGoParser.Access_fieldContext,0)


        def expression_array(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_arrayContext,0)


        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def expression_string(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_stringContext,0)


        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_term_plus

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_plus" ):
                return visitor.visitTerm_plus(self)
            else:
                return visitor.visitChildren(self)




    def term_plus(self):

        localctx = MiniGoParser.Term_plusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term_plus)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(MiniGoParser.STRING_LITERALS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.access_field(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 180
                self.expression_array()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 181
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 182
                self.expression_string(0)
                self.state = 183
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_float(self):
            return self.getTypedRuleContext(MiniGoParser.Add_floatContext,0)


        def expression_float(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_floatContext,0)


        def relational(self):
            return self.getTypedRuleContext(MiniGoParser.RelationalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_float

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_float" ):
                return visitor.visitExpression_float(self)
            else:
                return visitor.visitChildren(self)



    def expression_float(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression_floatContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression_float, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.add_float(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression_floatContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_float)
                    self.state = 190
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 191
                    self.relational()
                    self.state = 192
                    self.add_float(0) 
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_float(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_floatContext,0)


        def add_float(self):
            return self.getTypedRuleContext(MiniGoParser.Add_floatContext,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_add_float

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_float" ):
                return visitor.visitAdd_float(self)
            else:
                return visitor.visitChildren(self)



    def add_float(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Add_floatContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_add_float, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.mul_float(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Add_floatContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_float)
                    self.state = 202
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 203
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 204
                    self.mul_float(0) 
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_float(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_floatContext,0)


        def mul_float(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_floatContext,0)


        def MULTIPLY(self):
            return self.getToken(MiniGoParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(MiniGoParser.DIVIDE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mul_float

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_float" ):
                return visitor.visitMul_float(self)
            else:
                return visitor.visitChildren(self)



    def mul_float(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Mul_floatContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_mul_float, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.unary_float()
            self._ctx.stop = self._input.LT(-1)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Mul_floatContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_float)
                    self.state = 213
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 214
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.MULTIPLY or _la==MiniGoParser.DIVIDE):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 215
                    self.unary_float() 
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Unary_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def unary_float(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_floatContext,0)


        def term_float(self):
            return self.getTypedRuleContext(MiniGoParser.Term_floatContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unary_float

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_float" ):
                return visitor.visitUnary_float(self)
            else:
                return visitor.visitChildren(self)




    def unary_float(self):

        localctx = MiniGoParser.Unary_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_unary_float)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(MiniGoParser.MINUS)
                self.state = 222
                self.unary_float()
                pass
            elif token in [MiniGoParser.LEFT_SQUARE_BRACKET, MiniGoParser.LEFT_PARENTHESES, MiniGoParser.INT_LITERALS, MiniGoParser.FLOAT_LITERALS, MiniGoParser.STRING_LITERALS, MiniGoParser.BOOLEAN_LITERALS, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.term_float()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def FLOAT_LITERALS(self):
            return self.getToken(MiniGoParser.FLOAT_LITERALS, 0)

        def INT_LITERALS(self):
            return self.getToken(MiniGoParser.INT_LITERALS, 0)

        def access_field(self):
            return self.getTypedRuleContext(MiniGoParser.Access_fieldContext,0)


        def expression_array(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_arrayContext,0)


        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def expression_float(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_floatContext,0)


        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_term_float

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_float" ):
                return visitor.visitTerm_float(self)
            else:
                return visitor.visitChildren(self)




    def term_float(self):

        localctx = MiniGoParser.Term_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_term_float)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(MiniGoParser.FLOAT_LITERALS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.match(MiniGoParser.INT_LITERALS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 229
                self.access_field(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 230
                self.expression_array()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 231
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 232
                self.expression_float(0)
                self.state = 233
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_int(self):
            return self.getTypedRuleContext(MiniGoParser.Add_intContext,0)


        def expression_int(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_intContext,0)


        def relational(self):
            return self.getTypedRuleContext(MiniGoParser.RelationalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_int" ):
                return visitor.visitExpression_int(self)
            else:
                return visitor.visitChildren(self)



    def expression_int(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression_intContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expression_int, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.add_int(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 246
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression_intContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_int)
                    self.state = 240
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 241
                    self.relational()
                    self.state = 242
                    self.add_int(0) 
                self.state = 248
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_int(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_intContext,0)


        def add_int(self):
            return self.getTypedRuleContext(MiniGoParser.Add_intContext,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_add_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_int" ):
                return visitor.visitAdd_int(self)
            else:
                return visitor.visitChildren(self)



    def add_int(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Add_intContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_add_int, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.mul_int(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Add_intContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_int)
                    self.state = 252
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 253
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 254
                    self.mul_int(0) 
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_int(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_intContext,0)


        def mul_int(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_intContext,0)


        def MULTIPLY(self):
            return self.getToken(MiniGoParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(MiniGoParser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(MiniGoParser.MODULO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mul_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_int" ):
                return visitor.visitMul_int(self)
            else:
                return visitor.visitChildren(self)



    def mul_int(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Mul_intContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_mul_int, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.unary_int()
            self._ctx.stop = self._input.LT(-1)
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Mul_intContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_int)
                    self.state = 263
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 264
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULTIPLY) | (1 << MiniGoParser.DIVIDE) | (1 << MiniGoParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 265
                    self.unary_int() 
                self.state = 270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Unary_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def unary_int(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_intContext,0)


        def term_int(self):
            return self.getTypedRuleContext(MiniGoParser.Term_intContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unary_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_int" ):
                return visitor.visitUnary_int(self)
            else:
                return visitor.visitChildren(self)




    def unary_int(self):

        localctx = MiniGoParser.Unary_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_unary_int)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(MiniGoParser.MINUS)
                self.state = 272
                self.unary_int()
                pass
            elif token in [MiniGoParser.LEFT_SQUARE_BRACKET, MiniGoParser.LEFT_PARENTHESES, MiniGoParser.INT_LITERALS, MiniGoParser.FLOAT_LITERALS, MiniGoParser.STRING_LITERALS, MiniGoParser.BOOLEAN_LITERALS, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.term_int()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT_LITERALS(self):
            return self.getToken(MiniGoParser.INT_LITERALS, 0)

        def access_field(self):
            return self.getTypedRuleContext(MiniGoParser.Access_fieldContext,0)


        def expression_array(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_arrayContext,0)


        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def expression_int(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_intContext,0)


        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_term_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_int" ):
                return visitor.visitTerm_int(self)
            else:
                return visitor.visitChildren(self)




    def term_int(self):

        localctx = MiniGoParser.Term_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_term_int)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(MiniGoParser.INT_LITERALS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 278
                self.access_field(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 279
                self.expression_array()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 280
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 281
                self.expression_int(0)
                self.state = 282
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_booleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.And_booleanContext,0)


        def expression_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_booleanContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_boolean

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_boolean" ):
                return visitor.visitExpression_boolean(self)
            else:
                return visitor.visitChildren(self)



    def expression_boolean(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression_booleanContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression_boolean, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.and_boolean(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression_booleanContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_boolean)
                    self.state = 289
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 290
                    self.match(MiniGoParser.OR)
                    self.state = 291
                    self.and_boolean(0) 
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class And_booleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compare_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Compare_booleanContext,0)


        def and_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.And_booleanContext,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_and_boolean

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_boolean" ):
                return visitor.visitAnd_boolean(self)
            else:
                return visitor.visitChildren(self)



    def and_boolean(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.And_booleanContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_and_boolean, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.compare_boolean(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.And_booleanContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_boolean)
                    self.state = 300
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 301
                    self.match(MiniGoParser.AND)
                    self.state = 302
                    self.compare_boolean(0) 
                self.state = 307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Compare_booleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_booleanContext,0)


        def compare_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Compare_booleanContext,0)


        def DOUBLE_EQUAL(self):
            return self.getToken(MiniGoParser.DOUBLE_EQUAL, 0)

        def DIFFERENT_EQUAL(self):
            return self.getToken(MiniGoParser.DIFFERENT_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_compare_boolean

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare_boolean" ):
                return visitor.visitCompare_boolean(self)
            else:
                return visitor.visitChildren(self)



    def compare_boolean(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Compare_booleanContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_compare_boolean, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.unary_boolean()
            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Compare_booleanContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_compare_boolean)
                    self.state = 311
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 312
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.DOUBLE_EQUAL or _la==MiniGoParser.DIFFERENT_EQUAL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 313
                    self.unary_boolean() 
                self.state = 318
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Unary_booleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIFFERENT(self):
            return self.getToken(MiniGoParser.DIFFERENT, 0)

        def unary_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_booleanContext,0)


        def term_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Term_booleanContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unary_boolean

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_boolean" ):
                return visitor.visitUnary_boolean(self)
            else:
                return visitor.visitChildren(self)




    def unary_boolean(self):

        localctx = MiniGoParser.Unary_booleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_unary_boolean)
        try:
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DIFFERENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(MiniGoParser.DIFFERENT)
                self.state = 320
                self.unary_boolean()
                pass
            elif token in [MiniGoParser.LEFT_SQUARE_BRACKET, MiniGoParser.LEFT_PARENTHESES, MiniGoParser.MINUS, MiniGoParser.INT_LITERALS, MiniGoParser.FLOAT_LITERALS, MiniGoParser.STRING_LITERALS, MiniGoParser.BOOLEAN_LITERALS, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.term_boolean()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_booleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN_LITERALS(self):
            return self.getToken(MiniGoParser.BOOLEAN_LITERALS, 0)

        def expression_int(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_intContext,0)


        def expression_float(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_floatContext,0)


        def expression_string(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_stringContext,0)


        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def expression_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_booleanContext,0)


        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_term_boolean

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_boolean" ):
                return visitor.visitTerm_boolean(self)
            else:
                return visitor.visitChildren(self)




    def term_boolean(self):

        localctx = MiniGoParser.Term_booleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_term_boolean)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.match(MiniGoParser.BOOLEAN_LITERALS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.expression_int(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 326
                self.expression_float(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 327
                self.expression_string(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 328
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 329
                self.expression_boolean(0)
                self.state = 330
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrays_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arrays_typeContext,0)


        def LEFT_BRACE(self):
            return self.getToken(MiniGoParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MiniGoParser.RIGHT_BRACE, 0)

        def array_instance(self):
            return self.getTypedRuleContext(MiniGoParser.Array_instanceContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_array" ):
                return visitor.visitExpression_array(self)
            else:
                return visitor.visitChildren(self)




    def expression_array(self):

        localctx = MiniGoParser.Expression_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.arrays_type()
            self.state = 335
            self.match(MiniGoParser.LEFT_BRACE)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DIFFERENT) | (1 << MiniGoParser.LEFT_SQUARE_BRACKET) | (1 << MiniGoParser.LEFT_BRACE) | (1 << MiniGoParser.LEFT_PARENTHESES) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.INT_LITERALS) | (1 << MiniGoParser.FLOAT_LITERALS) | (1 << MiniGoParser.STRING_LITERALS) | (1 << MiniGoParser.BOOLEAN_LITERALS) | (1 << MiniGoParser.ID))) != 0):
                self.state = 336
                self.array_instance()


            self.state = 339
            self.match(MiniGoParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_int(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_intContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_size" ):
                return visitor.visitArray_size(self)
            else:
                return visitor.visitChildren(self)




    def array_size(self):

        localctx = MiniGoParser.Array_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.expression_int(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arrays_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIMITIVE_TYPE(self):
            return self.getToken(MiniGoParser.PRIMITIVE_TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LEFT_SQUARE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LEFT_SQUARE_BRACKET)
            else:
                return self.getToken(MiniGoParser.LEFT_SQUARE_BRACKET, i)

        def array_size(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_sizeContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_sizeContext,i)


        def RIGHT_SQUARE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RIGHT_SQUARE_BRACKET)
            else:
                return self.getToken(MiniGoParser.RIGHT_SQUARE_BRACKET, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrays_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrays_type" ):
                return visitor.visitArrays_type(self)
            else:
                return visitor.visitChildren(self)




    def arrays_type(self):

        localctx = MiniGoParser.Arrays_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arrays_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 343
                self.match(MiniGoParser.LEFT_SQUARE_BRACKET)
                self.state = 344
                self.array_size()
                self.state = 345
                self.match(MiniGoParser.RIGHT_SQUARE_BRACKET)
                self.state = 349 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LEFT_SQUARE_BRACKET):
                    break

            self.state = 351
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.PRIMITIVE_TYPE or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_instanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_valueContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_valueContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_instance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_instance" ):
                return visitor.visitArray_instance(self)
            else:
                return visitor.visitChildren(self)




    def array_instance(self):

        localctx = MiniGoParser.Array_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_instance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.array_value()
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__0:
                self.state = 354
                self.match(MiniGoParser.T__0)
                self.state = 355
                self.array_value()
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_booleanContext,0)


        def expression_int(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_intContext,0)


        def expression_float(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_floatContext,0)


        def expression_string(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_stringContext,0)


        def struct_value(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_valueContext,0)


        def LEFT_BRACE(self):
            return self.getToken(MiniGoParser.LEFT_BRACE, 0)

        def array_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_valueContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_valueContext,i)


        def RIGHT_BRACE(self):
            return self.getToken(MiniGoParser.RIGHT_BRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value" ):
                return visitor.visitArray_value(self)
            else:
                return visitor.visitChildren(self)




    def array_value(self):

        localctx = MiniGoParser.Array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_array_value)
        self._la = 0 # Token type
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.expression_boolean(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.expression_int(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 363
                self.expression_float(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 364
                self.expression_string(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 365
                self.struct_value()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 366
                self.match(MiniGoParser.LEFT_BRACE)
                self.state = 367
                self.array_value()
                self.state = 372
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__0:
                    self.state = 368
                    self.match(MiniGoParser.T__0)
                    self.state = 369
                    self.array_value()
                    self.state = 374
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 375
                self.match(MiniGoParser.RIGHT_BRACE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 377
                self.match(MiniGoParser.LEFT_BRACE)
                self.state = 378
                self.match(MiniGoParser.RIGHT_BRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_idxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_booleanContext,0)


        def expression_int(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_intContext,0)


        def expression_float(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_floatContext,0)


        def expression_string(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_stringContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_idx

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_idx" ):
                return visitor.visitArray_idx(self)
            else:
                return visitor.visitChildren(self)




    def array_idx(self):

        localctx = MiniGoParser.Array_idxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_idx)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.expression_boolean(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.expression_int(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 383
                self.expression_float(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 384
                self.expression_string(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_access_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_name(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_nameContext,0)


        def LEFT_SQUARE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LEFT_SQUARE_BRACKET)
            else:
                return self.getToken(MiniGoParser.LEFT_SQUARE_BRACKET, i)

        def array_idx(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_idxContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_idxContext,i)


        def RIGHT_SQUARE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RIGHT_SQUARE_BRACKET)
            else:
                return self.getToken(MiniGoParser.RIGHT_SQUARE_BRACKET, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access_field" ):
                return visitor.visitArray_access_field(self)
            else:
                return visitor.visitChildren(self)




    def array_access_field(self):

        localctx = MiniGoParser.Array_access_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_array_access_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.arr_name()
            self.state = 392 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 388
                    self.match(MiniGoParser.LEFT_SQUARE_BRACKET)
                    self.state = 389
                    self.array_idx()
                    self.state = 390
                    self.match(MiniGoParser.RIGHT_SQUARE_BRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 394 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def callfuncdecl(self):
            return self.getTypedRuleContext(MiniGoParser.CallfuncdeclContext,0)


        def INT_LITERALS(self):
            return self.getToken(MiniGoParser.INT_LITERALS, 0)

        def FLOAT_LITERALS(self):
            return self.getToken(MiniGoParser.FLOAT_LITERALS, 0)

        def STRING_LITERALS(self):
            return self.getToken(MiniGoParser.STRING_LITERALS, 0)

        def BOOLEAN_LITERALS(self):
            return self.getToken(MiniGoParser.BOOLEAN_LITERALS, 0)

        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def expression_int(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_intContext,0)


        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def expression_float(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_floatContext,0)


        def expression_string(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_stringContext,0)


        def expression_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_booleanContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_name" ):
                return visitor.visitArr_name(self)
            else:
                return visitor.visitChildren(self)




    def arr_name(self):

        localctx = MiniGoParser.Arr_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arr_name)
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.callfuncdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 398
                self.match(MiniGoParser.INT_LITERALS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 399
                self.match(MiniGoParser.FLOAT_LITERALS)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 400
                self.match(MiniGoParser.STRING_LITERALS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 401
                self.match(MiniGoParser.BOOLEAN_LITERALS)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 402
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 403
                self.expression_int(0)
                self.state = 404
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 406
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 407
                self.expression_float(0)
                self.state = 408
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 410
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 411
                self.expression_string(0)
                self.state = 412
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 414
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 415
                self.expression_boolean(0)
                self.state = 416
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def callfuncdecl(self):
            return self.getTypedRuleContext(MiniGoParser.CallfuncdeclContext,0)


        def field(self):
            return self.getTypedRuleContext(MiniGoParser.FieldContext,0)


        def access_field(self):
            return self.getTypedRuleContext(MiniGoParser.Access_fieldContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_access_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess_field" ):
                return visitor.visitAccess_field(self)
            else:
                return visitor.visitChildren(self)



    def access_field(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Access_fieldContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_access_field, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 421
                self.callfuncdecl()
                pass

            elif la_ == 2:
                self.state = 422
                self.field()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 433
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 431
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Access_fieldContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_access_field)
                        self.state = 425
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 426
                        self.match(MiniGoParser.DOT)
                        self.state = 427
                        self.field()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Access_fieldContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_access_field)
                        self.state = 428
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 429
                        self.match(MiniGoParser.DOT)
                        self.state = 430
                        self.callfuncdecl()
                        pass

             
                self.state = 435
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_access_field(self):
            return self.getTypedRuleContext(MiniGoParser.Array_access_fieldContext,0)


        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def expression_int(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_intContext,0)


        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def expression_float(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_floatContext,0)


        def expression_string(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_stringContext,0)


        def expression_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_booleanContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_field)
        try:
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.array_access_field()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 438
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 439
                self.expression_int(0)
                self.state = 440
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 442
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 443
                self.expression_float(0)
                self.state = 444
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 446
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 447
                self.expression_string(0)
                self.state = 448
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 450
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 451
                self.expression_boolean(0)
                self.state = 452
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LEFT_BRACE(self):
            return self.getToken(MiniGoParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MiniGoParser.RIGHT_BRACE, 0)

        def field_value(self):
            return self.getTypedRuleContext(MiniGoParser.Field_valueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_value" ):
                return visitor.visitStruct_value(self)
            else:
                return visitor.visitChildren(self)




    def struct_value(self):

        localctx = MiniGoParser.Struct_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_struct_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.match(MiniGoParser.ID)
            self.state = 457
            self.match(MiniGoParser.LEFT_BRACE)
            self.state = 459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 458
                self.field_value()


            self.state = 461
            self.match(MiniGoParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COLONS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COLONS)
            else:
                return self.getToken(MiniGoParser.COLONS, i)

        def value_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Value_assignContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Value_assignContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_value" ):
                return visitor.visitField_value(self)
            else:
                return visitor.visitChildren(self)




    def field_value(self):

        localctx = MiniGoParser.Field_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_field_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(MiniGoParser.ID)
            self.state = 464
            self.match(MiniGoParser.COLONS)
            self.state = 465
            self.value_assign()
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__0:
                self.state = 466
                self.match(MiniGoParser.T__0)
                self.state = 467
                self.match(MiniGoParser.ID)
                self.state = 468
                self.match(MiniGoParser.COLONS)
                self.state = 469
                self.value_assign()
                self.state = 474
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SMALLER(self):
            return self.getToken(MiniGoParser.SMALLER, 0)

        def SMALLER_EQUAL(self):
            return self.getToken(MiniGoParser.SMALLER_EQUAL, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def GREATER_EQUAL(self):
            return self.getToken(MiniGoParser.GREATER_EQUAL, 0)

        def DOUBLE_EQUAL(self):
            return self.getToken(MiniGoParser.DOUBLE_EQUAL, 0)

        def DIFFERENT_EQUAL(self):
            return self.getToken(MiniGoParser.DIFFERENT_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = MiniGoParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SMALLER) | (1 << MiniGoParser.SMALLER_EQUAL) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.GREATER_EQUAL) | (1 << MiniGoParser.DOUBLE_EQUAL) | (1 << MiniGoParser.DIFFERENT_EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Other_operationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS_EQUAL(self):
            return self.getToken(MiniGoParser.PLUS_EQUAL, 0)

        def MINUS_EQUAL(self):
            return self.getToken(MiniGoParser.MINUS_EQUAL, 0)

        def MULTIPLY_EQUAL(self):
            return self.getToken(MiniGoParser.MULTIPLY_EQUAL, 0)

        def DIVIDE_EQUAL(self):
            return self.getToken(MiniGoParser.DIVIDE_EQUAL, 0)

        def MODULO_EQUAL(self):
            return self.getToken(MiniGoParser.MODULO_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_other_operations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOther_operations" ):
                return visitor.visitOther_operations(self)
            else:
                return visitor.visitChildren(self)




    def other_operations(self):

        localctx = MiniGoParser.Other_operationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_other_operations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PLUS_EQUAL) | (1 << MiniGoParser.MINUS_EQUAL) | (1 << MiniGoParser.MULTIPLY_EQUAL) | (1 << MiniGoParser.DIVIDE_EQUAL) | (1 << MiniGoParser.MODULO_EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 479
                self.decl()
                self.state = 482 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.LEFT_PARENTHESES) | (1 << MiniGoParser.INT_LITERALS) | (1 << MiniGoParser.FLOAT_LITERALS) | (1 << MiniGoParser.STRING_LITERALS) | (1 << MiniGoParser.BOOLEAN_LITERALS) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 484
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def shortvardecl(self):
            return self.getTypedRuleContext(MiniGoParser.ShortvardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_decl)
        try:
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.constdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 488
                self.shortvardecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 489
                self.funcdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 490
                self.structdecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 491
                self.interfacedecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def LEFT_BRACE(self):
            return self.getToken(MiniGoParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MiniGoParser.RIGHT_BRACE, 0)

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def funcType(self):
            return self.getTypedRuleContext(MiniGoParser.FuncTypeContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(MiniGoParser.FUNC)
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LEFT_PARENTHESES:
                self.state = 495
                self.receiver()


            self.state = 498
            self.match(MiniGoParser.ID)
            self.state = 499
            self.match(MiniGoParser.LEFT_PARENTHESES)
            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 500
                self.funcParams()


            self.state = 503
            self.match(MiniGoParser.RIGHT_PARENTHESES)
            self.state = 505
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PRIMITIVE_TYPE) | (1 << MiniGoParser.LEFT_SQUARE_BRACKET) | (1 << MiniGoParser.ID))) != 0):
                self.state = 504
                self.funcType()


            self.state = 507
            self.match(MiniGoParser.LEFT_BRACE)
            self.state = 509 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 508
                self.block()
                self.state = 511 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN_WORD) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.LEFT_PARENTHESES) | (1 << MiniGoParser.INT_LITERALS) | (1 << MiniGoParser.FLOAT_LITERALS) | (1 << MiniGoParser.STRING_LITERALS) | (1 << MiniGoParser.BOOLEAN_LITERALS) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 513
            self.match(MiniGoParser.RIGHT_BRACE)
            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON:
                self.state = 514
                self.match(MiniGoParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcParam(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamContext,0)


        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcParams

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParams" ):
                return visitor.visitFuncParams(self)
            else:
                return visitor.visitChildren(self)




    def funcParams(self):

        localctx = MiniGoParser.FuncParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_funcParams)
        try:
            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 517
                self.funcParam()
                self.state = 518
                self.match(MiniGoParser.T__0)
                self.state = 519
                self.funcParams()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 521
                self.funcParam()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcListName(self):
            return self.getTypedRuleContext(MiniGoParser.FuncListNameContext,0)


        def funcType(self):
            return self.getTypedRuleContext(MiniGoParser.FuncTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcParam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParam" ):
                return visitor.visitFuncParam(self)
            else:
                return visitor.visitChildren(self)




    def funcParam(self):

        localctx = MiniGoParser.FuncParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_funcParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.funcListName()
            self.state = 525
            self.funcType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncListNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funcListName(self):
            return self.getTypedRuleContext(MiniGoParser.FuncListNameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcListName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncListName" ):
                return visitor.visitFuncListName(self)
            else:
                return visitor.visitChildren(self)




    def funcListName(self):

        localctx = MiniGoParser.FuncListNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_funcListName)
        try:
            self.state = 531
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.match(MiniGoParser.ID)
                self.state = 528
                self.match(MiniGoParser.T__0)
                self.state = 529
                self.funcListName()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 530
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIMITIVE_TYPE(self):
            return self.getToken(MiniGoParser.PRIMITIVE_TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrays_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arrays_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncType" ):
                return visitor.visitFuncType(self)
            else:
                return visitor.visitChildren(self)




    def funcType(self):

        localctx = MiniGoParser.FuncTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_funcType)
        try:
            self.state = 536
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.PRIMITIVE_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self.match(MiniGoParser.PRIMITIVE_TYPE)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 534
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LEFT_SQUARE_BRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 535
                self.arrays_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def shortvardecl(self):
            return self.getTypedRuleContext(MiniGoParser.ShortvardeclContext,0)


        def returndecl(self):
            return self.getTypedRuleContext(MiniGoParser.ReturndeclContext,0)


        def ifelsedecl(self):
            return self.getTypedRuleContext(MiniGoParser.IfelsedeclContext,0)


        def forloopdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ForloopdeclContext,0)


        def access_field(self):
            return self.getTypedRuleContext(MiniGoParser.Access_fieldContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_block)
        try:
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.constdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 540
                self.shortvardecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 541
                self.returndecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 542
                self.ifelsedecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 543
                self.forloopdecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 544
                self.access_field(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 545
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(MiniGoParser.LEFT_PARENTHESES)
            self.state = 549
            self.match(MiniGoParser.ID)
            self.state = 550
            self.match(MiniGoParser.ID)
            self.state = 551
            self.match(MiniGoParser.RIGHT_PARENTHESES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LEFT_BRACE(self):
            return self.getToken(MiniGoParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MiniGoParser.RIGHT_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def struct_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_fieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_structdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(MiniGoParser.TYPE)
            self.state = 554
            self.match(MiniGoParser.ID)
            self.state = 555
            self.match(MiniGoParser.STRUCT)
            self.state = 556
            self.match(MiniGoParser.LEFT_BRACE)
            self.state = 558 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 557
                self.struct_field()
                self.state = 560 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 562
            self.match(MiniGoParser.RIGHT_BRACE)
            self.state = 563
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def struct_fieldType(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldTypeContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_struct_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.match(MiniGoParser.ID)
            self.state = 566
            self.struct_fieldType()
            self.state = 567
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIMITIVE_TYPE(self):
            return self.getToken(MiniGoParser.PRIMITIVE_TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrays_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arrays_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_fieldType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_fieldType" ):
                return visitor.visitStruct_fieldType(self)
            else:
                return visitor.visitChildren(self)




    def struct_fieldType(self):

        localctx = MiniGoParser.Struct_fieldTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_struct_fieldType)
        try:
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.PRIMITIVE_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 569
                self.match(MiniGoParser.PRIMITIVE_TYPE)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 570
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LEFT_SQUARE_BRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 571
                self.arrays_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LEFT_BRACE(self):
            return self.getToken(MiniGoParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MiniGoParser.RIGHT_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def interface_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Interface_fieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Interface_fieldContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacedecl" ):
                return visitor.visitInterfacedecl(self)
            else:
                return visitor.visitChildren(self)




    def interfacedecl(self):

        localctx = MiniGoParser.InterfacedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_interfacedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(MiniGoParser.TYPE)
            self.state = 575
            self.match(MiniGoParser.ID)
            self.state = 576
            self.match(MiniGoParser.INTERFACE)
            self.state = 577
            self.match(MiniGoParser.LEFT_BRACE)
            self.state = 579 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 578
                self.interface_field()
                self.state = 581 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 583
            self.match(MiniGoParser.RIGHT_BRACE)
            self.state = 584
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def interfaceParams(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceParamsContext,0)


        def interfaceType(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_field" ):
                return visitor.visitInterface_field(self)
            else:
                return visitor.visitChildren(self)




    def interface_field(self):

        localctx = MiniGoParser.Interface_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_interface_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(MiniGoParser.ID)
            self.state = 587
            self.match(MiniGoParser.LEFT_PARENTHESES)
            self.state = 589
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 588
                self.interfaceParams()


            self.state = 591
            self.match(MiniGoParser.RIGHT_PARENTHESES)
            self.state = 593
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PRIMITIVE_TYPE) | (1 << MiniGoParser.LEFT_SQUARE_BRACKET) | (1 << MiniGoParser.ID))) != 0):
                self.state = 592
                self.interfaceType()


            self.state = 595
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfaceParam(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceParamContext,0)


        def interfaceParams(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceParamsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceParams

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceParams" ):
                return visitor.visitInterfaceParams(self)
            else:
                return visitor.visitChildren(self)




    def interfaceParams(self):

        localctx = MiniGoParser.InterfaceParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_interfaceParams)
        try:
            self.state = 602
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 597
                self.interfaceParam()
                self.state = 598
                self.match(MiniGoParser.T__0)
                self.state = 599
                self.interfaceParams()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 601
                self.interfaceParam()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfaceListName(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceListNameContext,0)


        def interfaceType(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceParam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceParam" ):
                return visitor.visitInterfaceParam(self)
            else:
                return visitor.visitChildren(self)




    def interfaceParam(self):

        localctx = MiniGoParser.InterfaceParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_interfaceParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.interfaceListName()
            self.state = 605
            self.interfaceType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceListNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def interfaceListName(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceListNameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceListName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceListName" ):
                return visitor.visitInterfaceListName(self)
            else:
                return visitor.visitChildren(self)




    def interfaceListName(self):

        localctx = MiniGoParser.InterfaceListNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_interfaceListName)
        try:
            self.state = 611
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 607
                self.match(MiniGoParser.ID)
                self.state = 608
                self.match(MiniGoParser.T__0)
                self.state = 609
                self.interfaceListName()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 610
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIMITIVE_TYPE(self):
            return self.getToken(MiniGoParser.PRIMITIVE_TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrays_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arrays_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceType" ):
                return visitor.visitInterfaceType(self)
            else:
                return visitor.visitChildren(self)




    def interfaceType(self):

        localctx = MiniGoParser.InterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_interfaceType)
        try:
            self.state = 616
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.PRIMITIVE_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 613
                self.match(MiniGoParser.PRIMITIVE_TYPE)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 614
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LEFT_SQUARE_BRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 615
                self.arrays_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def varType(self):
            return self.getTypedRuleContext(MiniGoParser.VarTypeContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def value_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Value_assignContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 633
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 618
                self.match(MiniGoParser.VAR)
                self.state = 619
                self.match(MiniGoParser.ID)
                self.state = 620
                self.varType()
                self.state = 623
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.EQUAL:
                    self.state = 621
                    self.match(MiniGoParser.EQUAL)
                    self.state = 622
                    self.value_assign()


                self.state = 625
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 627
                self.match(MiniGoParser.VAR)
                self.state = 628
                self.match(MiniGoParser.ID)
                self.state = 629
                self.match(MiniGoParser.EQUAL)
                self.state = 630
                self.value_assign()
                self.state = 631
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIMITIVE_TYPE(self):
            return self.getToken(MiniGoParser.PRIMITIVE_TYPE, 0)

        def arrays_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arrays_typeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_varType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarType" ):
                return visitor.visitVarType(self)
            else:
                return visitor.visitChildren(self)




    def varType(self):

        localctx = MiniGoParser.VarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_varType)
        try:
            self.state = 638
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.PRIMITIVE_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 635
                self.match(MiniGoParser.PRIMITIVE_TYPE)
                pass
            elif token in [MiniGoParser.LEFT_SQUARE_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 636
                self.arrays_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 637
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def value_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Value_assignContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_constdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 640
            self.match(MiniGoParser.CONST)
            self.state = 641
            self.match(MiniGoParser.ID)
            self.state = 642
            self.match(MiniGoParser.EQUAL)
            self.state = 643
            self.value_assign()
            self.state = 644
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortvardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assign_operators(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorsContext,0)


        def value_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Value_assignContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_shortvardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShortvardecl" ):
                return visitor.visitShortvardecl(self)
            else:
                return visitor.visitChildren(self)




    def shortvardecl(self):

        localctx = MiniGoParser.ShortvardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_shortvardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            self.lhs()
            self.state = 647
            self.assign_operators()
            self.state = 648
            self.value_assign()
            self.state = 649
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def access_field(self):
            return self.getTypedRuleContext(MiniGoParser.Access_fieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_lhs)
        try:
            self.state = 653
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 651
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 652
                self.access_field(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def other_operations(self):
            return self.getTypedRuleContext(MiniGoParser.Other_operationsContext,0)


        def COLONS_EQUAL(self):
            return self.getToken(MiniGoParser.COLONS_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_operators" ):
                return visitor.visitAssign_operators(self)
            else:
                return visitor.visitChildren(self)




    def assign_operators(self):

        localctx = MiniGoParser.Assign_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_assign_operators)
        try:
            self.state = 657
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.PLUS_EQUAL, MiniGoParser.MINUS_EQUAL, MiniGoParser.MULTIPLY_EQUAL, MiniGoParser.DIVIDE_EQUAL, MiniGoParser.MODULO_EQUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 655
                self.other_operations()
                pass
            elif token in [MiniGoParser.COLONS_EQUAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 656
                self.match(MiniGoParser.COLONS_EQUAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturndeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_WORD(self):
            return self.getToken(MiniGoParser.RETURN_WORD, 0)

        def value_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Value_assignContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_returndecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturndecl" ):
                return visitor.visitReturndecl(self)
            else:
                return visitor.visitChildren(self)




    def returndecl(self):

        localctx = MiniGoParser.ReturndeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_returndecl)
        self._la = 0 # Token type
        try:
            self.state = 665
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 659
                self.match(MiniGoParser.RETURN_WORD)
                self.state = 660
                self.value_assign()
                self.state = 661
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 663
                self.match(MiniGoParser.RETURN_WORD)
                self.state = 664
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallfuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def argu_list(self):
            return self.getTypedRuleContext(MiniGoParser.Argu_listContext,0)


        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_callfuncdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallfuncdecl" ):
                return visitor.visitCallfuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def callfuncdecl(self):

        localctx = MiniGoParser.CallfuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_callfuncdecl)
        try:
            self.state = 680
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 667
                self.match(MiniGoParser.ID)
                self.state = 668
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 669
                self.argu_list()
                self.state = 670
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                self.state = 672
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 671
                    self.match(MiniGoParser.SEMICOLON)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 674
                self.match(MiniGoParser.ID)
                self.state = 675
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 676
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                self.state = 678
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                if la_ == 1:
                    self.state = 677
                    self.match(MiniGoParser.SEMICOLON)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argu_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Value_assignContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Value_assignContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argu_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgu_list" ):
                return visitor.visitArgu_list(self)
            else:
                return visitor.visitChildren(self)




    def argu_list(self):

        localctx = MiniGoParser.Argu_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_argu_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 682
            self.value_assign()
            self.state = 687
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__0:
                self.state = 683
                self.match(MiniGoParser.T__0)
                self.state = 684
                self.value_assign()
                self.state = 689
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_value(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_valueContext,0)


        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def expression_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_booleanContext,0)


        def expression_array(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_arrayContext,0)


        def expression_int(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_intContext,0)


        def expression_float(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_floatContext,0)


        def expression_string(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_stringContext,0)


        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def value_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Value_assignContext,0)


        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_value_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_assign" ):
                return visitor.visitValue_assign(self)
            else:
                return visitor.visitChildren(self)




    def value_assign(self):

        localctx = MiniGoParser.Value_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_value_assign)
        try:
            self.state = 701
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 690
                self.struct_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 691
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 692
                self.expression_boolean(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 693
                self.expression_array()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 694
                self.expression_int(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 695
                self.expression_float(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 696
                self.expression_string(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 697
                self.match(MiniGoParser.LEFT_PARENTHESES)
                self.state = 698
                self.value_assign()
                self.state = 699
                self.match(MiniGoParser.RIGHT_PARENTHESES)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakdecl" ):
                return visitor.visitBreakdecl(self)
            else:
                return visitor.visitChildren(self)




    def breakdecl(self):

        localctx = MiniGoParser.BreakdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_breakdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 703
            self.match(MiniGoParser.BREAK)
            self.state = 704
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continuedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuedecl" ):
                return visitor.visitContinuedecl(self)
            else:
                return visitor.visitChildren(self)




    def continuedecl(self):

        localctx = MiniGoParser.ContinuedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_continuedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(MiniGoParser.CONTINUE)
            self.state = 707
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfelsedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def expression_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_booleanContext,0)


        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def LEFT_BRACE(self):
            return self.getToken(MiniGoParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MiniGoParser.RIGHT_BRACE, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def elifdecls(self):
            return self.getTypedRuleContext(MiniGoParser.ElifdeclsContext,0)


        def elsedecl(self):
            return self.getTypedRuleContext(MiniGoParser.ElsedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifelsedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelsedecl" ):
                return visitor.visitIfelsedecl(self)
            else:
                return visitor.visitChildren(self)




    def ifelsedecl(self):

        localctx = MiniGoParser.IfelsedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_ifelsedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 709
            self.match(MiniGoParser.IF)
            self.state = 710
            self.match(MiniGoParser.LEFT_PARENTHESES)
            self.state = 711
            self.expression_boolean(0)
            self.state = 712
            self.match(MiniGoParser.RIGHT_PARENTHESES)
            self.state = 713
            self.match(MiniGoParser.LEFT_BRACE)
            self.state = 715 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 714
                self.block()
                self.state = 717 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN_WORD) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.LEFT_PARENTHESES) | (1 << MiniGoParser.INT_LITERALS) | (1 << MiniGoParser.FLOAT_LITERALS) | (1 << MiniGoParser.STRING_LITERALS) | (1 << MiniGoParser.BOOLEAN_LITERALS) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 719
            self.match(MiniGoParser.RIGHT_BRACE)
            self.state = 721
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON:
                self.state = 720
                self.match(MiniGoParser.SEMICOLON)


            self.state = 724
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.state = 723
                self.elifdecls()


            self.state = 727
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 726
                self.elsedecl()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifdeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ElifdeclContext,0)


        def elifdecls(self):
            return self.getTypedRuleContext(MiniGoParser.ElifdeclsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elifdecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifdecls" ):
                return visitor.visitElifdecls(self)
            else:
                return visitor.visitChildren(self)




    def elifdecls(self):

        localctx = MiniGoParser.ElifdeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_elifdecls)
        try:
            self.state = 733
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 729
                self.elifdecl()
                self.state = 730
                self.elifdecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 732
                self.elifdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def expression_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_booleanContext,0)


        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def LEFT_BRACE(self):
            return self.getToken(MiniGoParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MiniGoParser.RIGHT_BRACE, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_elifdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifdecl" ):
                return visitor.visitElifdecl(self)
            else:
                return visitor.visitChildren(self)




    def elifdecl(self):

        localctx = MiniGoParser.ElifdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_elifdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 735
            self.match(MiniGoParser.ELSE)
            self.state = 736
            self.match(MiniGoParser.IF)
            self.state = 737
            self.match(MiniGoParser.LEFT_PARENTHESES)
            self.state = 738
            self.expression_boolean(0)
            self.state = 739
            self.match(MiniGoParser.RIGHT_PARENTHESES)
            self.state = 740
            self.match(MiniGoParser.LEFT_BRACE)
            self.state = 742 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 741
                self.block()
                self.state = 744 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN_WORD) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.LEFT_PARENTHESES) | (1 << MiniGoParser.INT_LITERALS) | (1 << MiniGoParser.FLOAT_LITERALS) | (1 << MiniGoParser.STRING_LITERALS) | (1 << MiniGoParser.BOOLEAN_LITERALS) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 746
            self.match(MiniGoParser.RIGHT_BRACE)
            self.state = 748
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON:
                self.state = 747
                self.match(MiniGoParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def LEFT_BRACE(self):
            return self.getToken(MiniGoParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MiniGoParser.RIGHT_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elsedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsedecl" ):
                return visitor.visitElsedecl(self)
            else:
                return visitor.visitChildren(self)




    def elsedecl(self):

        localctx = MiniGoParser.ElsedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_elsedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 750
            self.match(MiniGoParser.ELSE)
            self.state = 751
            self.match(MiniGoParser.LEFT_BRACE)
            self.state = 753 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 752
                self.block()
                self.state = 755 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN_WORD) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.LEFT_PARENTHESES) | (1 << MiniGoParser.INT_LITERALS) | (1 << MiniGoParser.FLOAT_LITERALS) | (1 << MiniGoParser.STRING_LITERALS) | (1 << MiniGoParser.BOOLEAN_LITERALS) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 757
            self.match(MiniGoParser.RIGHT_BRACE)
            self.state = 758
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ifelsedecl_inside_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def expression_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_booleanContext,0)


        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def LEFT_BRACE(self):
            return self.getToken(MiniGoParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MiniGoParser.RIGHT_BRACE, 0)

        def block_inside_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Block_inside_loopContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Block_inside_loopContext,i)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def elifdecls_inside_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Elifdecls_inside_loopContext,0)


        def elsedecl_inside_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Elsedecl_inside_loopContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifelsedecl_inside_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelsedecl_inside_loop" ):
                return visitor.visitIfelsedecl_inside_loop(self)
            else:
                return visitor.visitChildren(self)




    def ifelsedecl_inside_loop(self):

        localctx = MiniGoParser.Ifelsedecl_inside_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_ifelsedecl_inside_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 760
            self.match(MiniGoParser.IF)
            self.state = 761
            self.match(MiniGoParser.LEFT_PARENTHESES)
            self.state = 762
            self.expression_boolean(0)
            self.state = 763
            self.match(MiniGoParser.RIGHT_PARENTHESES)
            self.state = 764
            self.match(MiniGoParser.LEFT_BRACE)
            self.state = 766 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 765
                self.block_inside_loop()
                self.state = 768 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN_WORD) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.LEFT_PARENTHESES) | (1 << MiniGoParser.INT_LITERALS) | (1 << MiniGoParser.FLOAT_LITERALS) | (1 << MiniGoParser.STRING_LITERALS) | (1 << MiniGoParser.BOOLEAN_LITERALS) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 770
            self.match(MiniGoParser.RIGHT_BRACE)
            self.state = 772
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON:
                self.state = 771
                self.match(MiniGoParser.SEMICOLON)


            self.state = 775
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                self.state = 774
                self.elifdecls_inside_loop()


            self.state = 778
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 777
                self.elsedecl_inside_loop()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elifdecls_inside_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifdecl_inside_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Elifdecl_inside_loopContext,0)


        def elifdecls_inside_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Elifdecls_inside_loopContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elifdecls_inside_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifdecls_inside_loop" ):
                return visitor.visitElifdecls_inside_loop(self)
            else:
                return visitor.visitChildren(self)




    def elifdecls_inside_loop(self):

        localctx = MiniGoParser.Elifdecls_inside_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_elifdecls_inside_loop)
        try:
            self.state = 784
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 780
                self.elifdecl_inside_loop()
                self.state = 781
                self.elifdecls_inside_loop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 783
                self.elifdecl_inside_loop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elifdecl_inside_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LEFT_PARENTHESES(self):
            return self.getToken(MiniGoParser.LEFT_PARENTHESES, 0)

        def expression_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_booleanContext,0)


        def RIGHT_PARENTHESES(self):
            return self.getToken(MiniGoParser.RIGHT_PARENTHESES, 0)

        def LEFT_BRACE(self):
            return self.getToken(MiniGoParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MiniGoParser.RIGHT_BRACE, 0)

        def block_inside_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Block_inside_loopContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Block_inside_loopContext,i)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_elifdecl_inside_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifdecl_inside_loop" ):
                return visitor.visitElifdecl_inside_loop(self)
            else:
                return visitor.visitChildren(self)




    def elifdecl_inside_loop(self):

        localctx = MiniGoParser.Elifdecl_inside_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_elifdecl_inside_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 786
            self.match(MiniGoParser.ELSE)
            self.state = 787
            self.match(MiniGoParser.IF)
            self.state = 788
            self.match(MiniGoParser.LEFT_PARENTHESES)
            self.state = 789
            self.expression_boolean(0)
            self.state = 790
            self.match(MiniGoParser.RIGHT_PARENTHESES)
            self.state = 791
            self.match(MiniGoParser.LEFT_BRACE)
            self.state = 793 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 792
                self.block_inside_loop()
                self.state = 795 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN_WORD) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.LEFT_PARENTHESES) | (1 << MiniGoParser.INT_LITERALS) | (1 << MiniGoParser.FLOAT_LITERALS) | (1 << MiniGoParser.STRING_LITERALS) | (1 << MiniGoParser.BOOLEAN_LITERALS) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 797
            self.match(MiniGoParser.RIGHT_BRACE)
            self.state = 799
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON:
                self.state = 798
                self.match(MiniGoParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elsedecl_inside_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def LEFT_BRACE(self):
            return self.getToken(MiniGoParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MiniGoParser.RIGHT_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def block_inside_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Block_inside_loopContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Block_inside_loopContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elsedecl_inside_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsedecl_inside_loop" ):
                return visitor.visitElsedecl_inside_loop(self)
            else:
                return visitor.visitChildren(self)




    def elsedecl_inside_loop(self):

        localctx = MiniGoParser.Elsedecl_inside_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_elsedecl_inside_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 801
            self.match(MiniGoParser.ELSE)
            self.state = 802
            self.match(MiniGoParser.LEFT_BRACE)
            self.state = 804 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 803
                self.block_inside_loop()
                self.state = 806 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN_WORD) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.LEFT_PARENTHESES) | (1 << MiniGoParser.INT_LITERALS) | (1 << MiniGoParser.FLOAT_LITERALS) | (1 << MiniGoParser.STRING_LITERALS) | (1 << MiniGoParser.BOOLEAN_LITERALS) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 808
            self.match(MiniGoParser.RIGHT_BRACE)
            self.state = 809
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForloopdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def LEFT_BRACE(self):
            return self.getToken(MiniGoParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MiniGoParser.RIGHT_BRACE, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def block_inside_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Block_inside_loopContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Block_inside_loopContext,i)


        def initialization(self):
            return self.getTypedRuleContext(MiniGoParser.InitializationContext,0)


        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def for_access_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.For_access_valueContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.For_access_valueContext,i)


        def COLONS_EQUAL(self):
            return self.getToken(MiniGoParser.COLONS_EQUAL, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def for_arr(self):
            return self.getTypedRuleContext(MiniGoParser.For_arrContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloopdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForloopdecl" ):
                return visitor.visitForloopdecl(self)
            else:
                return visitor.visitChildren(self)




    def forloopdecl(self):

        localctx = MiniGoParser.ForloopdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_forloopdecl)
        self._la = 0 # Token type
        try:
            self.state = 853
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 811
                self.match(MiniGoParser.FOR)
                self.state = 812
                self.condition()
                self.state = 813
                self.match(MiniGoParser.LEFT_BRACE)
                self.state = 815 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 814
                    self.block_inside_loop()
                    self.state = 817 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN_WORD) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.LEFT_PARENTHESES) | (1 << MiniGoParser.INT_LITERALS) | (1 << MiniGoParser.FLOAT_LITERALS) | (1 << MiniGoParser.STRING_LITERALS) | (1 << MiniGoParser.BOOLEAN_LITERALS) | (1 << MiniGoParser.ID))) != 0)):
                        break

                self.state = 819
                self.match(MiniGoParser.RIGHT_BRACE)
                self.state = 820
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 822
                self.match(MiniGoParser.FOR)
                self.state = 823
                self.initialization()
                self.state = 824
                self.match(MiniGoParser.SEMICOLON)
                self.state = 825
                self.condition()
                self.state = 826
                self.match(MiniGoParser.SEMICOLON)
                self.state = 827
                self.update()
                self.state = 828
                self.match(MiniGoParser.LEFT_BRACE)
                self.state = 830 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 829
                    self.block_inside_loop()
                    self.state = 832 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN_WORD) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.LEFT_PARENTHESES) | (1 << MiniGoParser.INT_LITERALS) | (1 << MiniGoParser.FLOAT_LITERALS) | (1 << MiniGoParser.STRING_LITERALS) | (1 << MiniGoParser.BOOLEAN_LITERALS) | (1 << MiniGoParser.ID))) != 0)):
                        break

                self.state = 834
                self.match(MiniGoParser.RIGHT_BRACE)
                self.state = 835
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 837
                self.match(MiniGoParser.FOR)
                self.state = 838
                self.for_access_value()
                self.state = 839
                self.match(MiniGoParser.T__0)
                self.state = 840
                self.for_access_value()
                self.state = 841
                self.match(MiniGoParser.COLONS_EQUAL)
                self.state = 842
                self.match(MiniGoParser.RANGE)
                self.state = 843
                self.for_arr()
                self.state = 844
                self.match(MiniGoParser.LEFT_BRACE)
                self.state = 846 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 845
                    self.block_inside_loop()
                    self.state = 848 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN_WORD) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.LEFT_PARENTHESES) | (1 << MiniGoParser.INT_LITERALS) | (1 << MiniGoParser.FLOAT_LITERALS) | (1 << MiniGoParser.STRING_LITERALS) | (1 << MiniGoParser.BOOLEAN_LITERALS) | (1 << MiniGoParser.ID))) != 0)):
                        break

                self.state = 850
                self.match(MiniGoParser.RIGHT_BRACE)
                self.state = 851
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_access_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def UNDERSCORE(self):
            return self.getToken(MiniGoParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_access_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_access_value" ):
                return visitor.visitFor_access_value(self)
            else:
                return visitor.visitChildren(self)




    def for_access_value(self):

        localctx = MiniGoParser.For_access_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_for_access_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 855
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression_array(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_arrayContext,0)


        def access_field(self):
            return self.getTypedRuleContext(MiniGoParser.Access_fieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_arr" ):
                return visitor.visitFor_arr(self)
            else:
                return visitor.visitChildren(self)




    def for_arr(self):

        localctx = MiniGoParser.For_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_for_arr)
        try:
            self.state = 860
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 857
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 858
                self.expression_array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 859
                self.access_field(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_inside_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def shortvardecl(self):
            return self.getTypedRuleContext(MiniGoParser.ShortvardeclContext,0)


        def returndecl(self):
            return self.getTypedRuleContext(MiniGoParser.ReturndeclContext,0)


        def ifelsedecl_inside_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Ifelsedecl_inside_loopContext,0)


        def breakdecl(self):
            return self.getTypedRuleContext(MiniGoParser.BreakdeclContext,0)


        def continuedecl(self):
            return self.getTypedRuleContext(MiniGoParser.ContinuedeclContext,0)


        def forloopdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ForloopdeclContext,0)


        def access_field(self):
            return self.getTypedRuleContext(MiniGoParser.Access_fieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block_inside_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_inside_loop" ):
                return visitor.visitBlock_inside_loop(self)
            else:
                return visitor.visitChildren(self)




    def block_inside_loop(self):

        localctx = MiniGoParser.Block_inside_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_block_inside_loop)
        try:
            self.state = 871
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 862
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 863
                self.constdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 864
                self.shortvardecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 865
                self.returndecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 866
                self.ifelsedecl_inside_loop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 867
                self.breakdecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 868
                self.continuedecl()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 869
                self.forloopdecl()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 870
                self.access_field(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLONS_EQUAL(self):
            return self.getToken(MiniGoParser.COLONS_EQUAL, 0)

        def value_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Value_assignContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self):

        localctx = MiniGoParser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 873
            self.match(MiniGoParser.ID)
            self.state = 874
            self.match(MiniGoParser.COLONS_EQUAL)
            self.state = 875
            self.value_assign()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_boolean(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_booleanContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 877
            self.expression_boolean(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def other_operations(self):
            return self.getTypedRuleContext(MiniGoParser.Other_operationsContext,0)


        def value_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Value_assignContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 879
            self.match(MiniGoParser.ID)
            self.state = 880
            self.other_operations()
            self.state = 881
            self.value_assign()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expression_string_sempred
        self._predicates[1] = self.plus_string_sempred
        self._predicates[3] = self.expression_float_sempred
        self._predicates[4] = self.add_float_sempred
        self._predicates[5] = self.mul_float_sempred
        self._predicates[8] = self.expression_int_sempred
        self._predicates[9] = self.add_int_sempred
        self._predicates[10] = self.mul_int_sempred
        self._predicates[13] = self.expression_boolean_sempred
        self._predicates[14] = self.and_boolean_sempred
        self._predicates[15] = self.compare_boolean_sempred
        self._predicates[26] = self.access_field_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_string_sempred(self, localctx:Expression_stringContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def plus_string_sempred(self, localctx:Plus_stringContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression_float_sempred(self, localctx:Expression_floatContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def add_float_sempred(self, localctx:Add_floatContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def mul_float_sempred(self, localctx:Mul_floatContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression_int_sempred(self, localctx:Expression_intContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def add_int_sempred(self, localctx:Add_intContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def mul_int_sempred(self, localctx:Mul_intContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def expression_boolean_sempred(self, localctx:Expression_booleanContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def and_boolean_sempred(self, localctx:And_booleanContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def compare_boolean_sempred(self, localctx:Compare_booleanContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         

    def access_field_sempred(self, localctx:Access_fieldContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 3)
         




