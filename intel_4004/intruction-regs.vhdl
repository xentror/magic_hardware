library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity instruction_reg is
    port (
        RW : in std_logic;
        DataIn : in std_logic_vector(3 downto 0);
        DataOut : out std_logic_vector(3 downto 0)
    );
end entity;

architecture behavior of instruction_reg is
    signal instr : std_logic_vector(7 downto 0);
    signal cpt : integer := 0;
begin

    process(RW)
    begin
        if RW = '1' then
            if cpt = 0 then
                DataOut <= instr(3 downto 0);
            else
                DataOut <= instr(7 downto 4);
            end if;
        else
            if cpt = 0 then
                instr(3 downto 0) <= DataIn;
            else
                instr(7 downto 4) <= DataIn;
            end if;
        end if;
        cpt <= (cpt + 1) mod 2;

    end process;

end architecture;
