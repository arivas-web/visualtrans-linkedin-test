# visualtrans-linkedin

Sistema de contenido LinkedIn de Visual Trans. Estructura: lo que la IA **lee** (`input/`) y lo que **genera** (`output/`, por meses).

```
input/                           ← documentos que lee la IA
├── inbox/
│   ├── INBOX.md                 ← único archivo que se edita a mano
│   └── INBOX_procesado.md       ← histórico de entradas ya incorporadas
├── empresa/
│   ├── Contexto_Visual_Trans.txt   ← productos, propuesta de valor, argumentario
│   └── Pains_Unificados.txt        ← pains numerados
├── eventos/
│   └── Eventos_Campañas.txt        ← ferias, webinars, normativas, campañas
└── voces/
    ├── Voz_VT.txt               ← empresa
    ├── Voz_Ceci.txt             ← Cecilio Labrada
    ├── Voz_Emma.txt             ← Emma González
    ├── Voz_Enrique.txt          ← Enrique Saa
    └── Voz_Laura.txt            ← Laura Díaz

output/                          ← lo que genera la IA
└── AAAA-MM/
    ├── briefing.md
    ├── calendario.md
    ├── posts/[perfil].md
    ├── validacion.md
    └── log-decisiones.md
```
