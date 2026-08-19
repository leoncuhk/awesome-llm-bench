import json
import unittest

from scripts.fetch_benchmark import (
    extract_next_data,
    parse_next_data,
    parse_top10,
)


class FetchBenchmarkTests(unittest.TestCase):
    def test_parse_current_next_data_payload(self) -> None:
        payload = {
            "props": {
                "pageProps": {
                    "lastUpdated": "August 18, 2026",
                    "leaderboard": [
                        {
                            "model": "GPT-5.6 Sol",
                            "slug": "gpt-5-6-sol",
                            "creator": "OpenAI",
                            "sourceType": "Proprietary",
                            "score": 91.9,
                        },
                        {
                            "model": "Open Model",
                            "slug": "open-model",
                            "creator": "Example",
                            "sourceType": "Open Weight",
                            "score": 88,
                        },
                    ],
                }
            }
        }

        top10, updated_at, total = parse_next_data(payload)

        self.assertEqual(updated_at, "2026-08-18")
        self.assertEqual(total, 2)
        self.assertEqual(top10[0], {
            "rank": 1,
            "model": "GPT-5.6 Sol",
            "model_url": "/models/gpt-5-6-sol",
            "provider": "OpenAI",
            "license": "Closed",
            "score": 91.9,
        })
        self.assertEqual(top10[1]["license"], "Open")

    def test_extract_next_data_script(self) -> None:
        payload = {"props": {"pageProps": {"leaderboard": []}}}
        html = (
            '<html><script type="application/json" id="__NEXT_DATA__">'
            + json.dumps(payload)
            + "</script></html>"
        )
        self.assertEqual(extract_next_data(html), payload)

    def test_parse_legacy_markdown_fallback(self) -> None:
        markdown = (
            "1\n\n[Legacy Model](/models/legacy-model)\n\n"
            "ProviderClosed\n\n90.5%\n\nUpdated August 1, 2026\n"
            "12 models"
        )
        top10, updated_at, total = parse_top10(markdown)
        self.assertEqual(top10[0]["model"], "Legacy Model")
        self.assertEqual(updated_at, "2026-08-01")
        self.assertEqual(total, 12)


if __name__ == "__main__":
    unittest.main()
