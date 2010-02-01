#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import \
     Text, Comment, Literal, Operator, Keyword, Name, String

class GherkinLexer(RegexLexer):
    """
    For `Gherkin <http://cukes.info/>` syntax.
    """
    name = 'Gherkin'
    aliases = ['Cucumber', 'cucumber', 'Gherkin', 'gherkin']
    filenames = ['*.feature']
    mimetypes = ['text/x-gherkin']

    feature_keywords_regexp  = ur'^(기능|機能|功能|フィーチャ|خاصية|תכונה|Функционалност|Функционал|Особина|Могућност|Özellik|Właściwość|Tính năng|Savybė|Požiadavka|Požadavek|Osobina|Ominaisuus|Omadus|OH HAI|Mogućnost|Mogucnost|Jellemző|Fīča|Funzionalità|Funktionalität|Funkcionalnost|Funkcionalitāte|Funcționalitate|Functionaliteit|Functionalitate|Funcionalidade|Fonctionnalité|Fitur|Feature|Egenskap|Egenskab|Crikey|Característica|Arwedd)(:)(.*)$'
    scenario_keywords_regexp = ur'^(\s*)(시나리오 개요|시나리오|배경|背景|場景大綱|場景|场景大纲|场景|劇本大綱|劇本|テンプレ|シナリオテンプレート|シナリオテンプレ|シナリオアウトライン|シナリオ|سيناريو مخطط|سيناريو|الخلفية|תרחיש|תבנית תרחיש|רקע|Тарих|Сценарио|Сценарий структураси|Сценарий|Структура сценарија|Структура сценария|Скица|Рамка на сценарий|Пример|Предыстория|Предистория|Позадина|Основа|Концепт|Контекст|Założenia|Tình huống|Tausta|Taust|Tapausaihio|Tapaus|Szenariogrundriss|Szenario|Szablon scenariusza|Stsenaarium|Struktura scenarija|Skica|Skenario konsep|Skenario|Situācija|Senaryo taslağı|Senaryo|Scénář|Scénario|Schema dello scenario|Scenārijs pēc parauga|Scenārijs|Scenár|Scenariusz|Scenariul de şablon|Scenariul de sablon|Scenariu|Scenario Outline|Scenario Amlinellol|Scenario|Scenarijus|Scenarijaus šablonas|Scenarij|Scenarie|Rerefons|Raamstsenaarium|Primer|Pozadí|Pozadina|Pozadie|Plan du scénario|Plan du Scénario|Osnova scénáře|Osnova|Náčrt Scénáře|Náčrt Scenáru|Mate|MISHUN SRSLY|MISHUN|Kịch bản|Kontext|Konteksts|Kontekstas|Kontekst|Koncept|Khung tình huống|Khung kịch bản|Háttér|Grundlage|Geçmiş|Forgatókönyv vázlat|Forgatókönyv|Esquema do Cenário|Esquema do Cenario|Esquema del escenario|Esquema de l\'escenari|Escenario|Escenari|Dasar|Contexto|Contexte|Contesto|Condiţii|Conditii|Cenário|Cenario|Cefndir|Bối cảnh|Blokes|Bakgrunn|Bakgrund|Baggrund|Background|B4|Antecedents|Antecedentes|All y\'all|Achtergrond|Abstrakt Scenario|Abstract Scenario)(:)(.*)$'
    examples_regexp          = ur'^(\s*)(예|例子|例|サンプル|امثلة|דוגמאות|Сценарији|Примери|Мисоллар|Значения|Örnekler|Voorbeelden|Variantai|Tapaukset|Scenarios|Scenariji|Scenarijai|Příklady|Példák|Príklady|Przykłady|Primjeri|Primeri|Piemēri|Pavyzdžiai|Paraugs|Juhtumid|Exemplos|Exemples|Exemplele|Exempel|Examples|Esempi|Enghreifftiau|Eksempler|Ejemplos|EXAMPLZ|Dữ liệu|Contoh|Cobber|Beispiele)(:)(.*)$'
    step_keywords_regexp     = ur'^(\s*)(하지만|조건|만일|그리고|그러면|那麼|那么|而且|當|当|前提|假設|假如|但是|但し|並且|もし|ならば|ただし|しかし|かつ|و |متى |لكن |عندما |ثم |بفرض |اذاً |כאשר |וגם |בהינתן |אזי |אז |אבל |Унда |То |Онда |Но |Лекин |Когато |Када |Кад |К тому же |И |Задато |Задати |Задате |Если |Допустим |Дадено |Ва |Бирок |Аммо |Али |Агар |А |Și |És |anrhegedig a |Zatati |Zakładając |Zadato |Zadate |Zadano |Zadani |Zadan |Yna |Ya know how |Ya gotta |Y |Wtedy |When y\'all |When |Wenn |WEN |Và |Ve |Und |Un |Thì |Then y\'all |Then |Tapi |Tak |Tada |Tad |Så |Stel |Soit |Siis |Si |Quando |Quand |Quan |Pryd |Pokud |Pokiaľ |Però |Pero |Pak |Oraz |Onda |Ond |Oletetaan |Og |Och |O zaman |Når |När |Niin |Nhưng |N |Mutta |Men |Mas |Maka |Majd |Mais |Maar |Ma |Lorsque |Lorsqu\'|Kun |Kuid |Kui |Khi |Keď |Ketika |Když |Kai |Kada |Kad |Jeżeli |Ja |Ir |I CAN HAZ |I |Ha |Givet |Given y\'all |Given |Gitt |Gegeven |Gegeben sei |Fakat |Eğer ki |Etant donné |Et |Então |Entonces |Entao |En |Eeldades |E |Duota |Donat |Donada |Diyelim ki |Dengan |De |Dato |Dar |Dann |Dan |Dado |Dacă |Daca |DEN |Când |Cuando |Cho |Cept |Cand |But y\'all |But |Biết |Bet |BUT |Atunci |And y\'all |And |Ama |Als |Alors |Allora |Ali |Aleshores |Ale |Akkor |Aber |AN |A také |A |\* )'

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
            (r"[^\|]", Name.Variable),
          ],
        'scenario_sections_on_stack': [
            (scenario_keywords_regexp, bygroups(Text, Name.Class, Name.Class, Name.Constant), "multiline_descriptions_on_stack"),
            ],
        'narrative': [
            include('scenario_sections_on_stack'),
            (r"(\s|.)", Name.Builtin),
          ],
        'table_vars': [
            (r'(<[^>]*>)', bygroups(Name.Variable)),
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
        'root': [
            (r'\n', Text),
            include('comments'),
            (r'"""', String, "py_string"),
            (r'"', String, "double_string"),
            include('table_vars'),
            (r'@[^@\s]+', Name.Namespace),
            (step_keywords_regexp, bygroups(Text, Keyword)),
            (feature_keywords_regexp, bygroups(Name.Class, Name.Class, Name.Constant), 'narrative'),
            (scenario_keywords_regexp, bygroups(Text, Name.Class, Name.Class, Name.Constant), "multiline_descriptions"),
            (examples_regexp, bygroups(Text, Name.Class, Name.Class, Name.Constant), "scenario_table_description"),
            (r'(\s|.)', Text),
        ]
    }
