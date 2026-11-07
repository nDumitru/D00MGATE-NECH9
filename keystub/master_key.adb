-- =============================================================
-- D00MGATE-NECH9 -- Master Key (PUBLIC STUB BODY)
-- Reads D00MGATE_MASTER_KEY from the environment. No secret here.
-- =============================================================

with Ada.Environment_Variables;
with Ada.Text_IO;
with GNAT.SHA256;

package body Master_Key is

   Env_Name : constant String := "D00MGATE_MASTER_KEY";

   function Value return String is
   begin
      if Ada.Environment_Variables.Exists (Env_Name)
        and then Ada.Environment_Variables.Value (Env_Name)'Length > 0
      then
         return Ada.Environment_Variables.Value (Env_Name);
      end if;
      return Placeholder;
   end Value;

   function Is_Ready return Boolean is
   begin
      return Value /= Placeholder;
   end Is_Ready;

   function Sign (Data : String) return String is
   begin
      return GNAT.SHA256.Digest (Value & ":" & Data);
   end Sign;

   procedure Warn (Context : String) is
   begin
      Ada.Text_IO.Put_Line
        ("[MASTER KEY] Not set - DEMO MODE (" & Context &
         "). Set " & Env_Name & " to activate.");
   end Warn;

   function Require (Operation : String) return Boolean is
   begin
      if Is_Ready then
         return True;
      end if;
      Warn (Operation);
      return False;
   end Require;

end Master_Key;
