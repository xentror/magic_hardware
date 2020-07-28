library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity alu is
    port (
        DataOut : out std_logic_vector(3 downto 0);
        A, B : in std_logic_vector(3 downto 0);
        Sel : in std_logic_vector(1 downto 0)
    );
end entity;

architecture behavior of alu is
begin

    process(A, B, Sel)
    begin

        case Sel is
            when "00" =>
                DataOut <= A;
            when "01" =>
                DataOut <= B;
            when "10" =>
                DataOut <= std_logic_vector(unsigned(A) + unsigned(B));
            when "11" =>
                DataOut <= std_logic_vector(unsigned(A) - unsigned(B));
            when others =>
                DataOut <= (others => 'Z');
        end case;
    end process;
end architecture;
