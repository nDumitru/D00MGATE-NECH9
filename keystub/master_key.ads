-- =============================================================
-- D00MGATE-NECH9 -- Master Key (PUBLIC STUB SPEC)
-- Author: Dumitru Nechita | License: D00MGATE-NECH9 Proprietary v1.0
--
-- No secret here. The key is read at start-up from the
-- environment variable D00MGATE_MASTER_KEY. Without it the
-- system runs in DEMO MODE.
--
-- A private body (core/master_key.adb, git-ignored) can be used
-- instead:  gprbuild -P doomgate.gpr -XDOOMGATE_KEY_DIR=core
-- =============================================================

package Master_Key is

   Placeholder : constant String := "MASTER_KEY_HERE";

   function Value return String;
   --  Current Master Key (Placeholder in demo mode).

   function Is_Ready return Boolean;
   --  True when a real Master Key is configured.

   function Sign (Data : String) return String;
   --  SHA-256 (hex, 64 chars) of Key & ":" & Data.

   procedure Warn (Context : String);
   --  Print the demo-mode warning.

   function Require (Operation : String) return Boolean;
   --  Gate for privileged operations. False (and a warning) in demo mode.

end Master_Key;
