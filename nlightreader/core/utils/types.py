type _PrimitiveType = str | bytes | int | float | bool
type _PrimitiveCollection = list[_PrimitiveType] | dict[str, _PrimitiveType]
type RequestParams = dict[
    _PrimitiveType,
    _PrimitiveType | _PrimitiveCollection,
]

type JSONValue = str | int | float | bool | JSONArray | JSONObject | None
type JSONObject = dict[str, JSONValue]
type JSONArray = list[JSONValue]

__all__ = ["JSONArray", "JSONObject", "JSONValue", "RequestParams"]
