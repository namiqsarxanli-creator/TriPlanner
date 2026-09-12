# TriPlanner — AI Səyahət Planlayıcısı

Terminal tətbiqi: şəhər, gün sayı, büdcə, səyahət tərzi və maraq sahələrini soruşur,
büdcəni kateqoriyalara (otel/yemək/nəqliyyat) bölür, sonra Gemini-dən **gündəlik
marşrut + 3 otel tövsiyəsi** (ekonom/orta/lüks) alır və nəticəni `.txt` faylına yazır.

## İşə salmaq

```bash
pip install -r requirements.txt
```

`.env.example` faylını `.env` kimi kopyalayın və `GEMINI_API_KEY`-i doldurun
(pulsuz: https://aistudio.google.com/apikey), sonra:

```bash
python trip_planner.py
```

## Necə işləyir

1. Büdcə analitikası: `daily_budget = budget / days`, sonra 40% otel, 30% yemək,
   30% nəqliyyat/muzey olaraq bölünür.
2. Maraq sahələri `set` ilə saxlanılır — istəməzsə istifadəçi bir kateqoriyanı
   (məs. `nightlife`) qara siyahıya sala bilər, `all_tags.difference(blacklist)`
   qalan kateqoriyaları Gemini-yə ötürür.
3. `generate_travel_plan()` bir dekoratorla (`log_api_call`) sarılıb — hər API
   çağırışının müddətini ölçüb loqlayır.
4. Nəticə Markdown formatında Azərbaycan dilində qaytarılır və fayla yazılır.

Kodda hazır (aktivləşdirilməmiş) bir n8n inteqrasiyası nümunəsi də var —
`send_to_n8n()` planı bir n8n webhook-una göndərməyə imkan verir.
