#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import \
     Text, Comment, Literal, Operator, Keyword, Name, String

class GherkinLexer(RegexLexer):
    name = 'Gherkin'
    aliases = ['Cucumber', 'cucumber', 'Gherkin', 'gherkin']
    filenames = ['*.feature', '*.story']

    feature_keywords_regexp  = ur'^(기능|機能|功能|フィーチャ|خاصية|תכונה|Функционалност|Функционал|Особина|Могућност|Özellik|Właściwość|Tính năng|Savybė|Požiadavka|Požadavek|Osobina|Ominaisuus|Omadus|OH HAI|Mogućnost|Mogucnost|Jellemző|Fīča|Funzionalità|Funktionalität|Funkcionalnost|Funkcionalitāte|Funcționalitate|Functionaliteit|Functionalitate|Funcionalidade|Fonctionnalité|Fitur|Feature|Egenskap|Egenskab|Crikey|Característica|Arwedd)(:)(.*)$'
    scenario_sections_regexp = ur'(\s+)(시나리오 개요|시나리오|배경|背景|場景大綱|場景|场景大纲|场景|劇本大綱|劇本|テンプレ|シナリオテンプレート|シナリオテンプレ|シナリオアウトライン|シナリオ|سيناريو مخطط|سيناريو|الخلفية|תרחיש|תבנית תרחיש|רקע|Тарих|Сценарио|Сценарий структураси|Сценарий|Структура сценарија|Структура сценария|Скица|Рамка на сценарий|Пример|Предыстория|Предистория|Позадина|Основа|Концепт|Контекст|Założenia|Tình huống|Tausta|Taust|Tapausaihio|Tapaus|Szenariogrundriss|Szenario|Szablon scenariusza|Stsenaarium|Struktura scenarija|Skica|Skenario konsep|Skenario|Situācija|Senaryo taslağı|Senaryo|Scénář|Scénario|Schema dello scenario|Scenārijs pēc parauga|Scenārijs|Scenár|Scenariusz|Scenariul de şablon|Scenariul de sablon|Scenariu|Scenario Outline|Scenario|Scenarijus|Scenarijaus šablonas|Scenarij|Scenarie|Rerefons|Raamstsenaarium|Primer|Pozadí|Pozadina|Pozadie|Plan du Scénario|Osnova scénáře|Osnova|Náčrt Scénáře|Náčrt Scenáru|Mate|MISHUN SRSLY|MISHUN|Kịch bản|Kontext|Konteksts|Kontekstas|Kontekst|Koncept|Khung tình huống|Khung kịch bản|Háttér|Grundlage|Geçmiş|Forgatókönyv vázlat|Forgatókönyv|Esquema do Cenário|Esquema do Cenario|Esquema del escenario|Esquema de l\'escenari|Escenario|Escenari|Dasar|Contexto|Contexte|Contesto|Condiţii|Conditii|Cenário|Cenario|Bối cảnh|Blokes|Bakgrunn|Bakgrund|Baggrund|Background|B4|Antecedents|Antecedentes|All y\'all|Achtergrond|Abstrakt Scenario|Abstract Scenario)(:)(.*)$'
    examples_regexp          = ur'(\s+)(예|例子|例|サンプル|امثلة|דוגמאות|Сценарији|Примери|Мисоллар|Значения|Örnekler|Voorbeelden|Variantai|Tapaukset|Scenarios|Scenariji|Scenarijai|Příklady|Példák|Príklady|Przykłady|Primjeri|Primeri|Piemēri|Pavyzdžiai|Paraugs|Juhtumid|Exemplos|Exemples|Exemplele|Exempel|Examples|Esempi|Enghreifftiau|Eksempler|Ejemplos|EXAMPLZ|Dữ liệu|Contoh|Cobber|Beispiele)(:)(.*)$'
    step_keywords_regexp     = ur'(\s+)(하지만|조건|만일|그리고|그러면|那麼|那么|而且|當|当|前提|假設|假如|但是|但し|並且|もし|ならば|ただし|しかし|かつ|و\s+|متى\s+|لكن\s+|عندما\s+|ثم\s+|بفرض\s+|اذاً\s+|כאשר\s+|וגם\s+|בהינתן\s+|אזי\s+|אז\s+|אבל\s+|Унда|То\s+|Онда\s+|Но\s+|Лекин|Когато\s+|Када\s+|Кад\s+|К тому же\s+|И\s+|Задато\s+|Задати\s+|Задате\s+|Если\s+|Допустим\s+|Дадено\s+|Ва|Бирок|Аммо|Али\s+|Агар|А\s+|Și\s+|És\s+|anrhegedig a\s+|Zatati\s+|Zakładając\s+|Zadato\s+|Zadate\s+|Zadano\s+|Zadani\s+|Zadan\s+|Yna\s+|Ya know how\s+|Ya gotta\s+|Y\s+|Wtedy\s+|When\s+|When y\'all\s+|Wenn\s+|WEN\s+|Và\s+|Ve|Und\s+|Un\s+|Thì\s+|Then\s+|Then y\'all\s+|Tapi\s+|Tak\s+|Tada\s+|Tad\s+|Så\s+|Soit\s+|Siis\s+|Si\s+|Quando\s+|Quan\s+|Pryd\s+|Pokud\s+|Pokiaľ\s+|Però\s+|Pero\s+|Pak\s+|Oraz\s+|Onda\s+|Ond\s+|Oletetaan\s+|Og\s+|Och\s+|O zaman|Når\s+|När\s+|Niin\s+|Nhưng\s+|N\s+|Mutta\s+|Men\s+|Mas\s+|Maka\s+|Majd\s+|Mais\s+|Maar\s+|Ma\s+|Lorsque\s+|Kun\s+|Kuid\s+|Kui\s+|Khi\s+|Keď\s+|Ketika\s+|Když\s+|Kai\s+|Kada\s+|Kad\s+|Jeżeli\s+|Ja\s+|Ir\s+|I\s+|I CAN HAZ\s+|Ha\s+|Givet\s+|Given\s+|Given y\'all\s+|Gitt\s+|Gegeven\s+|Gegeben sei\s+|Fakat|Eğer ki|Et\s+|Então\s+|Entonces\s+|Entao\s+|En\s+|Eeldades\s+|E\s+|Duota\s+|Donat\s+|Donada\s+|Diyelim ki|Dengan\s+|De\s+|Dato\s+|Dar\s+|Dann\s+|Dan\s+|Dado\s+|Dacă\s+|Daca\s+|DEN\s+|Când\s+|Cuando\s+|Cho\s+|Cept\s+|Cand\s+|But\s+|But y\'all\s+|Biết\s+|Bet\s+|BUT\s+|Atunci\s+|And\s+|And y\'all\s+|Ama|Als\s+|Alors\s+|Allora\s+|Ali\s+|Aleshores\s+|Ale\s+|Akkor\s+|Aber\s+|A\s+|AN\s+|A také\s+)'

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
            (r'(<[^>]*>)', bygroups(Literal.String.Symbol)),
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
            (step_keywords_regexp, bygroups(Text, Keyword)),
            (feature_keywords_regexp, bygroups(Name.Class, Name.Class, Name.Constant), 'narrative'),
            (scenario_sections_regexp, bygroups(Text, Name.Class, Name.Class, Name.Constant), "multiline_descriptions"),
            (examples_regexp, bygroups(Text, Name.Class, Name.Class, Name.Constant), "scenario_table_description"),
            (r'(\s|.)', Text),
        ]

    }
