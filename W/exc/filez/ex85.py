'''
Exercise work here 
'''

#  Beautification
from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
console = Console()


# Actual code logic here 

def ex85():
    """
    Solution for ex 85
    """
    console.print(Panel("""Chapter 85 - Writing functions""", 
                        border_style="red"))
    

    bann1 = """
[39m
[39m[38;2;176;239;89m [38;2;140;244;87m [38;2;118;247;93m█[38;2;108;245;107m█[38;2;98;240;127m█[38;2;90;230;150m█[38;2;83;217;172m█[38;2;77;201;192m█[38;2;72;184;208m╗[38;2;67;165;219m [38;2;63;148;224m [38;2;61;131;225m [38;2;72;116;222m█[38;2;82;104;216m█[38;2;90;93;208m█[38;2;97;84;199m█[38;2;101;78;192m█[38;2;104;73;185m╗[38;2;106;70;181m [38;2;107;68;178m [38;2;107;68;178m [38;2;107;69;179m█[38;2;105;71;183m█[38;2;103;75;188m█[38;2;99;80;195m█[38;2;94;87;203m█[38;2;88;96;211m╗[38;2;79;107;218m [38;2;69;120;223m [38;2;60;134;225m█[38;2;64;151;224m█[38;2;68;168;218m█[38;2;72;185;207m╗[38;2;77;202;191m [38;2;83;217;172m [38;2;90;230;150m [38;2;98;239;129m█[38;2;106;245;109m█[38;2;116;247;95m╗[38;2;132;245;87m [38;2;167;241;89m█[38;2;186;227;72m█[38;2;205;208;55m█[38;2;224;186;47m█[38;2;241;165;47m█[38;2;254;145;54m█[38;2;255;127;64m╗[38;2;255;112;78m 
[39m[38;2;178;237;85m [38;2;147;244;87m█[38;2;121;246;91m█[38;2;111;246;102m╔[38;2;101;242;120m═[38;2;93;234;141m═[38;2;86;223;162m═[38;2;80;209;183m═[38;2;74;192;201m╝[38;2;69;175;214m [38;2;65;157;222m [38;2;62;140;225m█[38;2;65;125;224m█[38;2;76;111;220m╔[38;2;85;99;213m═[38;2;93;89;205m═[38;2;98;82;197m█[38;2;103;76;189m█[38;2;105;72;183m╗[38;2;107;69;179m [38;2;108;68;177m█[38;2;108;68;177m█[38;2;107;69;179m╔[38;2;105;72;183m═[38;2;102;76;190m═[38;2;98;83;198m█[38;2;92;91;206m█[38;2;84;101;214m╗[38;2;74;113;221m [38;2;63;128;225m█[38;2;62;144;225m█[38;2;66;161;221m█[38;2;71;179;211m█[38;2;76;197;196m╗[38;2;82;214;177m [38;2;89;227;155m [38;2;97;238;132m█[38;2;105;244;111m█[38;2;116;247;95m║[38;2;132;245;87m [38;2;168;241;89m█[38;2;188;225;70m█[38;2;207;205;54m╔[38;2;227;182;46m═[38;2;244;160;48m═[38;2;255;139;57m█[38;2;255;121;70m█[38;2;255;106;85m╗
[39m[38;2;183;231;77m [38;2;161;242;88m█[38;2;130;245;88m█[38;2;116;247;95m║[38;2;107;245;109m [38;2;99;240;126m [38;2;91;232;146m█[38;2;85;220;167m█[38;2;79;207;186m█[38;2;74;191;202m╗[38;2;69;174;214m [38;2;65;157;222m█[38;2;62;141;225m█[38;2;64;126;224m█[38;2;74;113;221m█[38;2;83;102;215m█[38;2;90;92;208m█[38;2;96;85;200m█[38;2;100;79;194m║[38;2;103;76;189m [38;2;104;73;186m█[38;2;105;73;185m█[38;2;104;73;186m█[38;2;103;75;188m█[38;2;100;79;193m█[38;2;97;84;200m█[38;2;91;92;207m█[38;2;84;101;214m║[38;2;75;112;220m [38;2;64;126;224m█[38;2;62;141;225m█[38;2;66;159;222m╔[38;2;70;177;213m█[38;2;75;195;199m█[38;2;81;211;180m╗[38;2;88;226;157m [38;2;96;237;134m█[38;2;105;244;113m█[38;2;115;247;96m║[38;2;131;245;87m [38;2;169;241;89m█[38;2;189;225;70m█[38;2;209;203;53m║[38;2;229;179;46m [38;2;247;156;49m [38;2;255;135;59m█[38;2;255;116;74m█[38;2;255;101;90m║
[39m[38;2;193;220;65m [38;2;178;236;84m█[38;2;154;243;87m█[38;2;124;246;89m║[38;2;115;247;96m [38;2;107;245;108m [38;2;100;241;124m [38;2;93;234;142m█[38;2;87;224;161m█[38;2;81;211;180m║[38;2;76;197;196m [38;2;71;182;209m█[38;2;67;166;219m█[38;2;64;151;224m╔[38;2;61;136;225m═[38;2;67;123;224m═[38;2;75;112;220m█[38;2;83;102;215m█[38;2;88;95;210m║[38;2;93;89;205m [38;2;96;86;201m█[38;2;97;83;199m█[38;2;98;83;198m╔[38;2;97;84;199m═[38;2;95;87;202m═[38;2;91;91;207m█[38;2;86;98;212m█[38;2;80;106;217m║[38;2;72;116;222m [38;2;62;129;225m█[38;2;62;144;225m█[38;2;66;160;221m║[38;2;70;177;212m╚[38;2;75;195;199m█[38;2;81;211;180m█[38;2;88;225;158m╗[38;2;95;237;135m█[38;2;104;244;113m█[38;2;115;247;96m║[38;2;131;245;87m [38;2;169;241;89m█[38;2;189;224;69m█[38;2;209;202;52m║[38;2;230;178;46m [38;2;248;155;50m [38;2;255;133;60m█[38;2;255;114;76m█[38;2;255;99;93m║
[39m[38;2;208;203;53m [38;2;193;220;65m╚[38;2;180;234;81m█[38;2;163;242;88m█[38;2;133;245;87m█[38;2;119;246;92m█[38;2;112;246;101m█[38;2;104;244;113m█[38;2;98;239;129m╔[38;2;91;232;146m╝[38;2;86;222;164m [38;2;80;210;182m█[38;2;76;197;197m█[38;2;71;182;209m║[38;2;68;168;218m [38;2;64;154;223m [38;2;62;141;225m█[38;2;62;129;225m█[38;2;69;120;223m║[38;2;75;112;220m [38;2;80;106;217m█[38;2;83;102;215m█[38;2;85;100;213m║[38;2;85;99;213m [38;2;84;101;214m [38;2;81;104;216m█[38;2;77;109;219m█[38;2;72;116;222m║[38;2;65;126;224m [38;2;61;137;225m█[38;2;64;150;224m█[38;2;67;165;219m║[38;2;71;181;210m [38;2;76;197;196m╚[38;2;81;213;178m█[38;2;88;226;157m█[38;2;96;237;134m█[38;2;105;244;113m█[38;2;115;247;96m║[38;2;131;245;87m [38;2;169;241;89m█[38;2;189;224;69m█[38;2;209;202;52m█[38;2;230;178;46m█[38;2;248;155;50m█[38;2;255;133;60m█[38;2;255;114;76m╔[38;2;255;99;93m╝
[39m[38;2;229;180;46m [38;2;215;196;50m [38;2;202;211;57m╚[38;2;190;224;69m═[38;2;177;238;88m═[38;2;158;242;87m═[38;2;135;245;87m═[38;2;120;246;91m═[38;2;113;246;99m╝[38;2;106;245;110m [38;2;99;240;125m [38;2;93;234;141m╚[38;2;87;225;159m═[38;2;82;215;175m╝[38;2;78;202;191m [38;2;73;190;203m [38;2;70;177;213m╚[38;2;67;164;219m═[38;2;64;153;223m╝[38;2;62;143;225m [38;2;60;135;225m╚[38;2;63;128;225m═[38;2;66;124;224m╝[38;2;68;121;223m [38;2;68;121;223m [38;2;67;122;224m╚[38;2;64;126;224m═[38;2;60;131;225m╝[38;2;61;139;225m [38;2;63;149;224m╚[38;2;66;160;221m═[38;2;69;173;215m╝[38;2;73;187;205m [38;2;77;202;191m [38;2;83;216;174m╚[38;2;89;228;153m═[38;2;97;238;132m═[38;2;105;244;111m═[38;2;115;247;96m╝[38;2;132;245;87m [38;2;169;241;89m╚[38;2;189;225;70m═[38;2;208;203;53m═[38;2;229;180;46m═[38;2;246;157;49m═[38;2;255;135;59m═[38;2;255;116;73m╝[38;2;255;101;90m 
[39m
[39m
[39m
    """
    # Defining the function here 
    print(bann1)
    age = Prompt.ask("What is your age? Faggot ? :")
    def checkDriverAge(age) :
        """
        Sucking and fucking
        Args:
            age (_type_): _description_
        """
        if int(age) < 18:
            print("Sorry, you are too young to drive. Powering off")
        elif int(age) > 18:
            print("Powering On. Enjoy the ride!")
        else:
            print("Congratulations on your first year of driving. Enjoy!")
        
    checkDriverAge(age)
    rprint(checkDriverAge.__doc__)