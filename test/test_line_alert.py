"""line_aleart.pyのテスト"""
import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール
sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
import unittest
from app import line_alert

class TestLine_Alert(unittest.TestCase):

    def test(self):
        # ステータスコードが２００で返ってきているか
        APIK = line_alert.LINE_ALERT.sql()
        print(APIK)
        POST = line_alert.LINE_ALERT.line()
        print(POST)
        self.assertEqual(200, POST)

if __name__ == "__main__":
    unittest.main()