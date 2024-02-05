#include <cstdint>
#include <iostream>
#include <vector>
#include <bsoncxx/json.hpp>
#include <mongocxx/client.hpp>
#include <mongocxx/stdx.hpp>
#include <mongocxx/uri.hpp>
#include <mongocxx/instance.hpp>
#include <bsoncxx/builder/stream/helpers.hpp>
#include <bsoncxx/builder/stream/document.hpp>
#include <bsoncxx/builder/stream/array.hpp>
#include <bsoncxx/builder/basic/document.hpp>

using bsoncxx::builder::stream::close_array;
using bsoncxx::builder::stream::close_document;
using bsoncxx::builder::stream::document;
using bsoncxx::builder::stream::finalize;
using bsoncxx::builder::stream::open_array;
using bsoncxx::builder::stream::open_document;
using bsoncxx::builder::basic::kvp;
using bsoncxx::builder::basic::make_document;

int main() {
    try {
        mongocxx::instance instance{};
        mongocxx::uri uri("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.0.2");
        mongocxx::client client(uri);
        mongocxx::database db = client["KG_EntityMeasurement"];
        mongocxx::collection coll = db["Test_Metadata"];

        // /************************** Create and Insert Document ******************************/
        // auto doc = document{} << "SchemaType" << "EntityMeasurementMetadata"
        //                       << "SchemaVersion_EntityMeasurementMetadata" << 1
        //                       << "EntityID" << static_cast<int64_t>(2958549755423456)
        //                       << "Version" << static_cast<int64_t>(2958549862852355)
        //                       << "Name" << "Dataset/Measurementseries Metadata_2"
        //                       << "DynamicFields" << open_document
        //                           << "Filter" << "426Hz Filter Channel 3"
        //                           << "BAT-NR" << 48
        //                           << "Betriebszustand" << "SPI 3;3V; VDD3;3V"
        //                           << "Bewertung" << ""
        //                           << "Detektor / Modulation" << "CW 1;3s"
        //                           << "Ergebnisplot" << ""
        //                           << "Ergebnisplot 2" << ""
        //                           << "Frequenzbereich" << "100k -1G"
        //                           << "Messverfahren" << "DPI"
        //                           << "Prüfdatum/ Link" << ""

        //                           << "Schrittweite [MHz]" << open_array
        //                               << "0,1 ... 1 mit 0,01"
        //                               << "1 ... 10 mit 0,1"
        //                               << "10 ... 100 mit 1"
        //                               << "100 ... 1000 mit 5"
        //                               << "1000 ... 3200 mit 10"
        //                               << "3200 ... 6000 mit 20"
        //                           << close_array
                                  
        //                           << "Störgröße / Grenzwert" << "L20"
        //                           << "überwachung" << ""
        //                           << "Parameter" << open_document
        //                           << close_document
        //                           << "Quantity" << open_document
        //                           << close_document
        //                           << "LoggingMode" << "Logging PrüfTrig"
        //                           << "Filename" << "d:\PA_Brandl\Keks\Keks-A-sample\SCP\Dat\Keks_332.bin"
        //                           << "Comment" << ""
        //                           << "SmBox HW ID" << 6
        //                           << "SmBox SW ID" << 125
        //                           << "SmBox SerialNo" << 237
        //                           << "SmBox SW Vers" << "V4.4"
        //                           << "SmBox HW Vers" << "V1.0"
        //                           << "SCP SW Vers" << "V5.6.40.0"
        //                       << close_document
        //                       << finalize;

        // bsoncxx::stdx::optional<mongocxx::result::insert_one> result =
        //     coll.insert_one(doc.view());

        // if(result) {
        //     std::cout << "Inserted a new document with id: "
        //               << result->inserted_id().get_oid().value.to_string() << "\n";
        // } else {
        //     std::cout << "No document was inserted." << "\n";
        // }

        // /************************** Find Document by Field ******************************/
        // auto query = document{} << "EntityID" << static_cast<int64_t>(2958549755423456) << finalize;
        // bsoncxx::stdx::optional<bsoncxx::document::value> maybe_result = 
        //     coll.find_one(query.view());

        // if(maybe_result) {
        //     std::cout << "Found a document: "
        //             << bsoncxx::to_json(maybe_result->view()) << "\n";
        // } else {
        //     std::cout << "No document found with the specified criteria." << "\n";
        // }

        // /************************** Find Document by Array Element and Output ID Only ******************************/
        // // Create the query to match an array element
        // auto query = document{} << "DynamicFields.Schrittweite [MHz]" << open_document <<
        //                 "$elemMatch" << open_document <<
        //                     "$eq" << "1 ... 10 mit 0,1" <<
        //                 close_document <<
        //             close_document << finalize;

        // // Execute the find_one query
        // bsoncxx::stdx::optional<bsoncxx::document::value> maybe_result =
        //     coll.find_one(query.view());

        // // Output only the ID of the result
        // if(maybe_result) {
        //     auto view = maybe_result->view();
        //     auto id = view["_id"].get_oid().value.to_string(); // Extracting the ID
        //     std::cout << "Found a document ID: " << id << "\n";
        // } else {
        //     std::cout << "No document found with 'Schrittweite [MHz]' containing '1 ... 10 mit 0,1'." << "\n";
        // }

        // /************************** Update Field Value in a Subdocument ******************************/
        // // Create the filter to match the document with "DynamicFields.SmBox HW ID" equal to 6
        // auto filter = document{} << "DynamicFields.SmBox HW ID" << 6 << finalize;
        // // Create the update operation to set "DynamicFields.SmBox HW ID" to 10
        // auto update_operation = document{} << "$set" <<
        // open_document << "DynamicFields.SmBox HW ID" << 10 << close_document << finalize;

        // // Execute the update_one query
        // bsoncxx::stdx::optional<mongocxx::result::update> update_result =
        //     coll.update_one(filter.view(), update_operation.view());

        // // Output the result of the update operation
        // if(update_result) {
        //     std::cout << "Updated " << update_result->modified_count() << " document(s) 'SmBox HW ID' field to 10." << "\n";
        // } else {
        //     std::cout << "No document was updated - 'SmBox HW ID' field may not have been 6 or document does not exist." << "\n";
        // }

        // /************************** Delete Document by Field ******************************/
        // // Create the query to match the document to delete
        // auto delete_query = document{} << "DynamicFields.SmBox HW ID" << 6 << finalize;

        // // Execute the delete_one query
        // bsoncxx::stdx::optional<mongocxx::result::delete_result> delete_result =
        //     coll.delete_one(delete_query.view());

        // // Output the result of the delete operation
        // if(delete_result) {
        //     std::cout << "Deleted " << delete_result->deleted_count() << " document(s)." << "\n";
        // } else {
        //     std::cout << "No document was deleted." << "\n";
        // }
    }
    catch (const std::exception& e) {
        std::cout << "An exception occurred: " << e.what() << "\n";
    }

    return 0;
}
