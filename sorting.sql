create or replace function hot(score integer, date timestamp with time zone) returns numeric as $$
    select round(cast(log(greatest(abs($1), 1)) * sign($1) + (date_part('epoch', $2) - 1134028003) / 45000.0 as numeric), 7)
$$ language sql immutable;
