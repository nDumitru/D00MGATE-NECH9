"""Smoke tests: every public layer imports and runs in DEMO MODE."""
import importlib
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path[:0] = [ROOT, os.path.join(ROOT, "keystub")]

MODULES = [
    "genesis", "layer0_asimov", "layer1_identity", "layer2_routing", "layer3_transfer",
    "layer4_ledger", "layer5_fourraces", "layer6_defense", "layer7_irobot",
    "layer8_convergence", "layer9_omega49", "layer9_omega49_REVISED", "layer_evolution",
    "irobot_layers", "reverse_hydra", "historic_hardening", "veridex_layer10",
    "challenge", "challenge_demo", "challenge_demo_v020",
]


class TestImports(unittest.TestCase):
    def test_all_modules_import(self):
        for name in MODULES:
            with self.subTest(module=name):
                importlib.import_module(name)


class TestScripts(unittest.TestCase):
    def run_script(self, name, key=None):
        env = dict(os.environ)
        env.pop("D00MGATE_MASTER_KEY", None)
        if key:
            env["D00MGATE_MASTER_KEY"] = key
        return subprocess.run([sys.executable, "-W", "error::SyntaxWarning", name],
                              cwd=ROOT, env=env, input="", capture_output=True,
                              text=True, timeout=60)

    def test_layers_run_in_demo_and_full_mode(self):
        for name in MODULES[:-3]:
            for key in (None, "test-key"):
                with self.subTest(module=name, key=bool(key)):
                    r = self.run_script(name + ".py", key)
                    self.assertEqual(r.returncode, 0, r.stderr)

    def test_ctf_exits_cleanly_without_input(self):
        for name in ("challenge.py", "challenge_demo.py", "challenge_demo_v020.py"):
            with self.subTest(module=name):
                r = self.run_script(name)
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertIn("Session closed", r.stdout)


class TestMasterKeyStub(unittest.TestCase):
    def test_demo_mode(self):
        mk = importlib.import_module("master_key")
        self.assertEqual(len(mk.sign("x")), 64)
        if "D00MGATE_MASTER_KEY" not in os.environ:
            self.assertFalse(mk.ready())
            self.assertFalse(mk.require("test"))


class TestLuhn(unittest.TestCase):
    def test_luhn_checks(self):
        import challenge, challenge_demo, challenge_demo_v020
        for check in (challenge.luhn_check, challenge_demo._demo_luhn_check,
                      challenge_demo_v020._luhn_check):
            with self.subTest(check=check.__module__):
                self.assertTrue(check("79927398713"))
                self.assertFalse(check("79927398710"))
                self.assertFalse(check(""))
                self.assertFalse(check("12ab"))
                self.assertTrue(check(challenge.demo_token()))


if __name__ == "__main__":
    unittest.main()
