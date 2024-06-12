import React from "react"

const DiscList = ({ discs, updateDisc, updateCallback }) => {
    const onDelete = async (id) => {
        try {
            const options = {
                method: "DELETE"
            }
            const response = await fetch(`http://127.0.0.1:5000/delete_disc/${id}`, options)
            if (response.status === 200) {
                updateCallback()
            } else {
                console.error("Failed to delete")
            }
        } catch (error) {
            alert(error)
        }
    }

    return <div>
        <h2>Discs</h2>
        <table>
            <thead>
                <tr>
                    <th>Disc Brand</th>
                    <th>Disc Name</th>
                    <th>Speed</th>
                    <th>Glide</th>
                    <th>Turn</th>
                    <th>Fade</th>
                    <th>Plastic Type</th>
                    <th>Weight</th>
                    <th>Notes</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {discs.map((disc) => (
                    <tr key={disc.id}>
                        <td>{disc.disc_brand}</td>
                        <td>{disc.disc_name}</td>
                        <td>{disc.flight_speed}</td>
                        <td>{disc.flight_glide}</td>
                        <td>{disc.flight_turn}</td>
                        <td>{disc.flight_fade}</td>
                        <td>{disc.disc_plastic}</td>
                        <td>{disc.disc_weight}</td>
                        <td>{disc.disc_notes}</td>
                        <td>
                            <button onClick={() => updateDisc(disc)}>Update</button>
                            <button onClick={() => onDelete(disc.id)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default DiscList