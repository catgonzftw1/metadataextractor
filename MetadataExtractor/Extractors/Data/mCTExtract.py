from .IDataExtract import IDataExtract
from MetadataExtractor.Util import metadataCreation, metadataFormatter
import pydicom
from pathlib import Path
from pydicom._version import __version_info__
import logging

log = logging.getLogger(__name__)


class mCTExtract(IDataExtract):
    def extract(self, fileInfo):
        log.info('Extracting metadata for mCT file "' + fileInfo["file"] + '".')
        text = ""
        if file_name.lower().endswith('.mct'):
            with open(file, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    key_value = line.strip().split('=')
                    if len(key_value) == 2:
                        key = key_value[0].strip()
                        value = key_value[1].strip()
                        mCT_metadata[key] = value
            return mCT_metadata
        
        values = []
        identifier = fileInfo["identifier"]

        for attribute in attributes.keys():
            objectValue = attributes[attribute]
            values.append(
                {
                    "predicate": "mexattr:"
                    + metadataFormatter.replaceForbiddenValues(attribute),
                    "object": objectValue,
                }
            )

        metadata = metadataCreation.addEntryToFileGraph(
            fileInfo,
            self._IExtract__config,
            {
                "additionalPrefixes": [
                    "@prefix dcat: <http://www.w3.org/ns/dcat#>",
                    "@prefix dcterms: <http://purl.org/dc/terms/>",
                ],
                "identifier": identifier,
                "ontology": "mex",
                "values": values,
            },
        )

        return (text, metadata)

    def registerMimeTypes(self):
        self.mimeTypes["concrete"] = ["application/dcm"]
