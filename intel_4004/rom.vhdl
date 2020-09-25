library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ROM is
    port (
        ADDR: in std_logic_vector(12 downto 0); -- 4096 values
        RW : in std_logic;
        DataOut :  out std_logic_vector(7 downto 0);
        DataIn : in std_logic_vector(7 downto 0)
    );
end entity;

architecture behavior of ROM is
    type RAM is array(4095 downto 0) of std_logic_vector(7 downto 0);
    signal Data : RAM;
begin

    DataOut <= (others => 'Z');

    process(RW)
    begin
        if RW = '1' then
            Data(to_integer(unsigned(Addr))) <= DataIn;
        end if;

        DataOut <= Data(to_integer(unsigned(Addr)));
    end process;

end architecture;
