library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity subroutine is
    port (
        Sel, RW, Back : in std_logic;
        Data : inout std_logic_vector(3 downto 0);
        Reset : in std_logic
    );
end entity;

architecture behavior of subroutine is
    type Mem is array(3 downto 0) of std_logic_vector(11 downto 0);

    signal stack : Mem := (others => (others => '0'));
    signal ptr : integer := 0;
    signal size : integer := 1;

    signal cpt : integer := 0;
begin

    Data <= (others => 'Z');

    process(Sel, RW)
    begin

        if Sel = '1' then
            -- Read Program counter in 3 cycle
            if RW = '0' then
                if cpt = 0 then
                    Data <= stack(3)(3 downto 0);
                elsif cpt = 1 then
                    Data <= stack(3)(7 downto 4);
                else
                    Data <= stack(3)(11 downto 8);
                end if;
                cpt <= (cpt + 1) mod 4;

            -- Branch back subroutine
            elsif Back = '0' and size >= 1 then
                ptr <= ptr - 1;
                size <= size - 1;

                if ptr < 0 then
                    ptr <= 3;
                end if;

                stack(3) <= stack(ptr);

            -- Branch in subroutine in 3 cycle
            else
                if cpt = 0 then
                    -- Write return address (PC + 4) at ptr position
                    stack(ptr) <= std_logic_vector(unsigned(stack(3)) + 4);

                    -- Update size and ptr
                    if size < 4 then
                        size <= size + 1;
                    end if;
                    ptr <= (ptr + 1) mod 4;

                    -- Updates new PC value
                    stack(3)(3 downto 0) <= Data;

                elsif cpt = 1 then
                    stack(3)(7 downto 4) <= Data;
                else
                    stack(3)(11 downto 8) <= Data;
                end if;
                cpt <= (cpt + 1) mod 4;

            end if;
        end if;

    end process;
end architecture;
