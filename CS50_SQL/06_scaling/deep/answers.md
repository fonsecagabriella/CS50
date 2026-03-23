# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

- Positive points: Balance load between boats;
- Negative points: One will need to search in all the boats to find data needed;

## Partitioning by Hour

- Positive points: One can search only in boat according to partition and data needed;
- Negative points: Unbalanced load between boats; some boats might be completly empty due to partition definition.

## Partitioning by Hash Value

- Positive points: Balanced value between boats; One can search only the database needed based on the partioning;
- Negative points: The partioning needs to match the hash value; therefore it's necessary extra processing of the timestamp to a hash value.
