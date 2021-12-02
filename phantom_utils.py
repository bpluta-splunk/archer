# File: phantom_utils.py
#
# Copyright (c) 2016-2021 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
def get_blank_container():
    '''Returns a blank container per [the docs]/docs/rest/create_container'''
    return {'asset_id': 0,
            'data': {},
            'description': '',
            'due_time': '',
            'label': '',
            'name': '',
            'owner_id': '',
            'sensitivity': '',
            'severity': '',
            'source_data_identifier': '',
            'status': '',
            'start_time': '',
            'tags': []}.copy()


def get_blank_artifact():
    '''Returns a blank artifact per [the docs]/docs/rest/artifacts'''
    return {'asset_id': None,
            'cef': {
                'ApplicationProtocol': '',
                'act': '',
                'app': '',
                'baseEventCount': '',
                'bytesIn': '',
                'bytesOut': '',
                'cat': '',
                'cn1': '',
                'cn1Label': '',
                'cn2': '',
                'cn2Label': '',
                'cn3': '',
                'cn3Label': '',
                'cnt': '',
                'cs1': '',
                'cs1Label': '',
                'cs2': '',
                'cs2Label': '',
                'cs3': '',
                'cs3Label': '',
                'cs4': '',
                'cs4Label': '',
                'cs5': '',
                'cs5Label': '',
                'cs6': '',
                'cs6Label': '',
                'destinationAddress': '',
                'destinationDnsDomain': '',
                'destinationHostName': '',
                'destinationMacAddress': '',
                'destinationNtDomain': '',
                'destinationPort': '',
                'destinationProcessName': '',
                'destinationServiceName': '',
                'destinationTranslatedAddress': '',
                'destinationTranslatedPort': '',
                'destinationUserId': '',
                'destinationUserName': '',
                'destinationUserPrivileges': '',
                'deviceAction': '',
                'deviceAddress': '',
                'deviceCustomDate1': '',
                'deviceCustomDate1Label': '',
                'deviceCustomDate2': '',
                'deviceCustomDate2Label': '',
                'deviceCustomNumber1': '',
                'deviceCustomNumber1Label': '',
                'deviceCustomNumber2': '',
                'deviceCustomNumber2Label': '',
                'deviceCustomNumber3': '',
                'deviceCustomNumber3Label': '',
                'deviceCustomString1': '',
                'deviceCustomString1Label': '',
                'deviceCustomString2': '',
                'deviceCustomString2Label': '',
                'deviceCustomString3': '',
                'deviceCustomString3Label': '',
                'deviceCustomString4': '',
                'deviceCustomString4Label': '',
                'deviceCustomString5': '',
                'deviceCustomString5Label': '',
                'deviceCustomString6': '',
                'deviceCustomString6Label': '',
                'deviceDirection': '',
                'deviceDnsDomain': '',
                'deviceEventCategory': '',
                'deviceExternalId': '',
                'deviceFacility': '',
                'deviceHostname': '',
                'deviceInboundInterface': '',
                'deviceMacAddress': '',
                'deviceOutboundInterface': '',
                'deviceProcessName': '',
                'deviceTranslatedAddress': '',
                'dhost': '',
                'dmac': '',
                'dntdom': '',
                'dpriv': '',
                'dproc': '',
                'dpt': '',
                'dst': '',
                'duid': '',
                'duser': '',
                'dvc': '',
                'dvchost': '',
                'end': '',
                'endTime': '',
                'externalId': '',
                'fileCreateTime': '',
                'fileHash': '',
                'fileId': '',
                'fileModificationTime': '',
                'fileName': '',
                'filePath': '',
                'filePermission': '',
                'fileSize': '',
                'fileType': '',
                'fname': '',
                'fsize': '',
                'in': '',
                'message': '',
                'method': '',
                'msg': '',
                'oldfileCreateTime': '',
                'oldfileHash': '',
                'oldfileId': '',
                'oldfileModificationTime': '',
                'oldfileName': '',
                'oldfilePath': '',
                'oldfilePermission': '',
                'oldfileType': '',
                'oldfsize': '',
                'out': '',
                'proto': '',
                'receiptTime': '',
                'request': '',
                'requestClientApplication': '',
                'requestCookies': '',
                'requestMethod': '',
                'requestURL': '',
                'rt': '',
                'shost': '',
                'smac': '',
                'sntdom': '',
                'sourceAddress': '',
                'sourceDnsDomain': '',
                'sourceHostName': '',
                'sourceMacAddress': '',
                'sourceNtDomain': '',
                'sourcePort': '',
                'sourceServiceName': '',
                'sourceTranslatedAddress': '',
                'sourceTranslatedPort': '',
                'sourceUserId': '',
                'sourceUserName': '',
                'sourceUserPrivileges': '',
                'spriv': '',
                'spt': '',
                'src': '',
                'start': '',
                'startTime': '',
                'suid': '',
                'suser': '',
                'transportProtocol': ''},
            'container_id': None,
            'data': {},
            'end_time': '',
            'label': '',
            'severity': '',
            'source_data_identifier': '',
            'start_time': '',
            'tags': [],
            'type': ''}.copy()
