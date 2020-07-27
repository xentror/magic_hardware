library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity registers is
    port (
        RW : in std_logic;
        Addr : in std_logic_vector(3 downto 0);
        Data : inout std_logic_vector(3 downto 0);
        Reset : in std_logic
    );
end entity;

architecture behavior of registers is
    type mem is array(15 downto 0) of std_logic_vector(3 downto 0);
    signal Regs : mem := (others => (others => '0'));
begin

    Data <= (others => 'Z');

    process(Addr, RW, Reset)
    begin
        if Reset = '1' then
            Regs <= (others => (others => '0'));
        elsif RW = '1' then
        Regs(to_integer(unsigned(Addr))) <= Data;
        else
            Data <= Regs(to_integer(unsigned(Addr)));
        end if;
    end process;

end architecture;
