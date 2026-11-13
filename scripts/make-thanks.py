#!/usr/bin/env python3
# SPDX-FileCopyrightText: BlueOS
# SPDX-License-Identifier: Apache-2.0
"""Makes THANKS.md and THANKS.ru.md from thanks.json — the one list behind «Настройки → О телефоне → Благодарности»,
the site's page and these two files. To add a person: edit thanks.json, run this script, commit both, push.
The phone and the site read thanks.json from the repository (branch main) every time: no new build.

thanks.json:
  {"people": [{"name": "...", "kind": "donate" | "help", "ru": "what they did", "en": "...", "link": "https://..."}],
   "donate": {"url": "https://...", "ru": "...", "en": "..."}}        # "link" and "donate" are optional
"""
import json, os, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXT = {
    'en': dict(file='THANKS.md', switch='**English** | [Русский](THANKS.ru.md)', title='Thanks',
               intro='BlueOS is made by one person in their free time. These people supported it or helped make it '
                     'better — thank you!',
               donors='Supported the project', helpers='Helped', support='Support BlueOS',
               empty='The list is empty for now.',
               note='This list is also on the phone («Settings → About phone → Thanks») and on the site. They all '
                    'read [`thanks.json`](thanks.json), so a new name shows up everywhere without a new build.'),
    'ru': dict(file='THANKS.ru.md', switch='[English](THANKS.md) | **Русский**', title='Благодарности',
               intro='BlueOS делает один человек в свободное время. Эти люди поддержали проект или помогли сделать '
                     'его лучше — спасибо им!',
               donors='Поддержали проект', helpers='Помогли', support='Поддержать BlueOS',
               empty='Пока здесь пусто.',
               note='Этот же список есть в телефоне («Настройки → О телефоне → Благодарности») и на сайте. Все они '
                    'читают [`thanks.json`](thanks.json), поэтому новое имя появляется везде без новой сборки.'),
}


def esc(s):
    return s.replace('|', '\\|').replace('\n', ' ').strip()


def person(p, lang):
    name = esc(p['name'])
    link = p.get('link', '')
    if link.startswith('https://'):
        name = f'[{name}]({link})'
    what = esc(p.get(lang) or p.get('en' if lang == 'ru' else 'ru') or '')
    return f'- **{name}**' + (f' — {what}' if what else '')


def main():
    data = json.load(open(os.path.join(HERE, 'thanks.json'), encoding='utf-8'))
    people = [p for p in data.get('people', []) if p.get('name', '').strip()]
    for lang, t in TEXT.items():
        out = [f'# {t["title"]}', '', t['switch'], '', t['intro'], '']
        donors = [p for p in people if p.get('kind') == 'donate']
        helpers = [p for p in people if p.get('kind') != 'donate']
        if not people:
            out += [t['empty'], '']
        for head, group in ((t['donors'], donors), (t['helpers'], helpers)):
            if group:
                out += [f'## {head}', ''] + [person(p, lang) for p in group] + ['']
        d = data.get('donate') or {}
        if d.get('url', '').startswith('https://'):
            out += [f'## {t["support"]}', '', f'[{esc(d.get(lang) or d["url"])}]({d["url"]})', '']
        out += [t['note'], '']
        open(os.path.join(HERE, t['file']), 'w', encoding='utf-8').write('\n'.join(out))
        print('wrote', t['file'], f'({len(people)} people)')


if __name__ == '__main__':
    sys.exit(main())
