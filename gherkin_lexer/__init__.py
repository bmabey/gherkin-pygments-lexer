#!/usr/bin/env python
from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import \
     Text, Comment, Literal, Operator, Keyword, Name, String

class GherkinLexer(RegexLexer):
    name = 'Gherkin'
    aliases = ['Cucumber', 'cucumber', 'Gherkin', 'gherkin']
    filenames = ['*.feature', '*.story']

    step_keywords_regexp = r'(하지만|조건|만일|그리고|그러면|那麼|那么|而且|當|当|前提|假設|假如|但是|但し|並且|もし|ならば|しかし|かつ|و\s+|متى\s+|لكن\s+|عندما\s+|ثم\s+|بفرض\s+|اذاً\s+|כאשר\s+|וגם\s+|בהינתן\s+|אזי\s+|אז\s+|אבל\s+|То\s+|Но\s+|Когато\s+|К тому же\s+|И\s+|Если\s+|Допустим\s+|Дадено\s+|А\s+|Și\s+|És\s+|anrhegedig a\s+|Zakładając\s+|Yna\s+|Ya know how\s+|Ya gotta\s+|Y\s+|Wtedy\s+|When\s+|When y\'all\s+|Wenn\s+|WEN\s+|Và\s+|Und\s+|Un\s+|Thì\s+|Then\s+|Then y\'all\s+|Tapi\s+|Tak\s+|Tada\s+|Tad\s+|Så\s+|Soit\s+|Siis\s+|Si\s+|Quando\s+|Quan\s+|Pryd\s+|Pokud\s+|Pokiaľ\s+|Però\s+|Pero\s+|Pak\s+|Oraz\s+|Ond\s+|Oletetaan\s+|Og\s+|Och\s+|Når\s+|När\s+|Niin\s+|Nhưng\s+|N\s+|Mutta\s+|Men\s+|Mas\s+|Maka\s+|Majd\s+|Mais\s+|Maar\s+|Ma\s+|Lorsque\s+|Kun\s+|Kuid\s+|Kui\s+|Khi\s+|Keď\s+|Ketika\s+|Když\s+|Kai\s+|Kad\s+|Jeżeli\s+|Ja\s+|Ir\s+|I\s+|I CAN HAZ\s+|Ha\s+|Givet\s+|Given\s+|Given y\'all\s+|Gitt\s+|Gegeven\s+|Gegeben sei\s+|Et\s+|Então\s+|Entonces\s+|Entao\s+|En\s+|Eeldades\s+|E\s+|Duota\s+|Donat\s+|Donada\s+|Dengan\s+|De\s+|Dato\s+|Dar\s+|Dann\s+|Dan\s+|Dado\s+|Dacă\s+|Daca\s+|DEN\s+|Când\s+|Cuando\s+|Cho\s+|Cept\s+|Cand\s+|But\s+|But y\'all\s+|Biết\s+|Bet\s+|BUT\s+|Atunci\s+|And\s+|And y\'all\s+|Als\s+|Alors\s+|Allora\s+|Aleshores\s+|Ale\s+|Akkor\s+|Aber\s+|A\s+|AN\s+|A také\s+)'
    scenario_sections_regexp = r'(\s+)(시나리오 개요|시나리오|배경|背景|場景大綱|場景|场景大纲|场景|劇本大綱|劇本|テンプレ|シナリオテンプレート|シナリオテンプレ|シナリオアウトライン|シナリオ|سيناريو مخطط|سيناريو|الخلفية|תרחיש|תבנית תרחיש|רקע|Сценарий|Структура сценария|Рамка на сценарий|Предыстория|Предистория|Założenia|Tình huống|Tausta|Taust|Tapausaihio|Tapaus|Szenariogrundriss|Szenario|Szablon scenariusza|Stsenaarium|Skenario konsep|Skenario|Situācija|Scénář|Scénario|Schema dello scenario|Scenārijs pēc parauga|Scenārijs|Scenár|Scenariusz|Scenariu|Scenario Outline|Scenario|Scenarijus|Scenarijaus šablonas|Scenarie|Rerefons|Raamstsenaarium|Pozadí|Pozadie|Plan du Scénario|Osnova scénáře|Náčrt Scénáře|Náčrt Scenáru|Mate|MISHUN SRSLY|MISHUN|Kịch bản|Kontext|Konteksts|Kontekstas|Khung tình huống|Khung kịch bản|Háttér|Grundlage|Forgatókönyv vázlat|Forgatókönyv|Esquema do Cenário|Esquema do Cenario|Esquema del escenario|Esquema de l\'escenari|Escenario|Escenari|Dasar|Contexto|Contexte|Contesto|Cenário|Cenario|Bối cảnh|Blokes|Bakgrunn|Bakgrund|Baggrund|Background|B4|Antecedents|Antecedentes|All y\'all|Achtergrond|Abstrakt Scenario|Abstract Scenario)(:)(.*)$'

    tokens = {
        'comments': [
            (r'#.*$', Comment),
          ],
        'multiline_descriptions' : [
            (step_keywords_regexp, Keyword, "#pop"),
            include('comments'),
            (r"(\s|.)", Name.Constant),
          ],
        'multiline_descriptions_on_stack' : [
          (step_keywords_regexp, Keyword, "#pop:2"),
            include('comments'),
            (r"(\s|.)", Name.Constant),
          ],
        'scenario_table_description': [
            (r"\s+\|", Text, 'scenario_table_header'),
            include('comments'),
            (r"(\s|.)", Name.Constant),
          ],
        'scenario_table_header': [
            (r"\s+\|\s*$", Text, "#pop:2"),
            (r"(\s+\|\s*)(#.*)$", bygroups(Text, Comment), "#pop:2"),
            include('comments'),
            (r"\s+\|", Text),
            (r"[^\|]", Literal.String.Symbol),
          ],
        'scenario_sections_on_stack': [
            (scenario_sections_regexp, bygroups(Text, Name.Class, Name.Class, Name.Constant), "multiline_descriptions_on_stack"),
            ],
        'narrative': [
            include('scenario_sections_on_stack'),
            (r"(\s|.)", Name.Builtin),
          ],
        'table_vars': [
            (r'(<)([^>]*)(>)', bygroups(Operator, Literal.String.Symbol, Operator)),
          ],
        'string': [
            include('table_vars'),
            (r'(\s|.)', String),
          ],
        'py_string': [
            (r'"""', String, "#pop"),
            include('string'),
          ],
        'double_string': [
            (r'"', String, "#pop"),
            include('string'),
          ],
        'single_string': [
            (r"'", String, "#pop"),
            include('string'),
          ],
        'root': [
            (r'\n', Text),
            include('comments'),
            (r'"""', String, "py_string"),
            (r'"', String, "double_string"),
            (r"'", String, "single_string"),
            include('table_vars'),
            (r'@[^@\s]+', Name.Namespace),
            (step_keywords_regexp, Keyword),
            (r'^(Feature|Story)(:)(.*)$', bygroups(Name.Class, Name.Class, Name.Constant), 'narrative'),
            (scenario_sections_regexp, bygroups(Text, Name.Class, Name.Class, Name.Constant), "multiline_descriptions"),
            (r'(\s+)(Scenarios|Examples)(:)(.*)$', bygroups(Text, Name.Class, Name.Class, Name.Constant), "scenario_table_description"),
            (r'(\s|.)', Text),
        ]

    }
