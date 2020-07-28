library ieee;
library work;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity alu_block is
    port (
        -- Flags
        Flags : inout std_logic_vector(3 downto 0);

        -- Accumulator and Temporary Register
        AccIn, TempRegIn : in std_logic_vector(3 downto 0);
        WrEnAcc, WrEnTempReg :in std_logic;

        -- ALU
        SelAlu : in std_logic_vector(1 downto 0);
        AluOut : out std_logic_vector(3 downto 0);

        -- Reset
        Reset : in std_logic
    );
end entity;

architecture behavior of alu_block is
    signal Acc, TempReg : std_logic_vector(3 downto 0);
begin

    process(AccIn, WrEnAcc)
    begin
        if WrEnAcc = '1' then
            Acc <= AccIn;
        end if;
    end process;

    process(TempRegIn, WrEnTempReg)
    begin
        if WrEnTempReg = '1' then
            TempReg <= TempRegIn;
        end if;
    end process;

    ALU1 : entity work.alu
            port map (
                A => Acc,
                B => TempReg,
                DataOut => AluOut,
                Sel => SelAlu
            );
end architecture;
