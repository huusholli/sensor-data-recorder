# SENSOR-DATA-RECORDER

Simple sensor data recorder just to store all data for now.

## Installation

```
docker-compose up -d
```

## Data persistence

Data is written in CSV files, one file for each sensor. CSV files are located under `data` directory.

CSV structure is like follows, without headers, first value being the timestamp and second the value.

```
1598106776,990.79
1598106776,990.79
1598106777,990.13
1598106778,990.21
1598106778,990.24
1598106779,990.45
```

## Development

Using VS Code's Remote Containers is the preferred way of development. Configurations exists for that.

## License

MIT
