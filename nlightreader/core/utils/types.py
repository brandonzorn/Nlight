from collections.abc import Mapping, Sequence

type _PrimitiveType = str | bytes | int | float | bool
type _PrimitiveCollection = list[_PrimitiveType] | dict[str, _PrimitiveType]
type RequestParams = dict[
    _PrimitiveType,
    _PrimitiveType | _PrimitiveCollection,
]

type JSONValue = bool | int | float | str | JSONArray | JSONObject | None
type JSONObject = Mapping[str, JSONValue]
type JSONArray = Sequence[JSONValue]

type HTTPCookies = dict[str, str]
type HTTPHeaders = Mapping[str, str | bytes]
type HTTPData = Mapping[str, str]

__all__ = [
    "HTTPCookies",
    "HTTPData",
    "HTTPHeaders",
    "JSONArray",
    "JSONObject",
    "JSONValue",
    "RequestParams",
]
